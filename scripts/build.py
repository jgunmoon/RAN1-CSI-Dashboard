"""원본 DB를 읽어 CSI 리포트를 만듭니다 (자동 실행 진입점).

    python -m scripts.build                    # config의 원본 저장소에서 DB를 받아 reports/ 생성
    python -m scripts.build --db 파일.json     # 내려받은 DB 파일로 생성 (오프라인·테스트)

reports/index.html(HTML 대시보드), reports/README.md(요약), reports/by_topic/*.md(주제별 전체 결정),
reports/csi_decisions.json(고른 결정과 주제·범위 표시), reports/changes.json(직전 결과 대비 변경 이력)을 만듭니다.
같은 DB와 설정이면 같은 결과가 나오며, 결과가 달라진 실행에서만 변경 이력이 하나 늘어납니다.
--notify-file을 주면 변경이 있을 때 알림(GitHub Issue) 본문을 그 파일에 씁니다 (첫 줄이 제목).
"""
import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

import yaml

from scripts import changes, model, render_html, render_md, source

ROOT = Path(__file__).resolve().parent.parent


def load_config(path=ROOT / "config" / "csi_scope.yaml"):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def _read_json(path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return default


def build(config, db, out_dir, now=None, notify_file=None):
    m = model.build(db, config)
    if not m["meetings"]:
        raise ValueError("원본 DB에 회의가 없습니다")
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    keep = ("id", "meeting", "agenda_item", "agenda_title", "agenda_path", "type", "text", "ffs", "source",
            "scope", "topic", "tags", "keywords", "stage", "impact", "clauses", "warn")
    export = {"source_db": source.db_url(config), "source_updated_at": db.get("updated_at"), "topics": m["topics"],
              "entries": [{k: e.get(k) for k in keep} for e in m["entries"]]}
    now = now or datetime.now(timezone.utc).isoformat(timespec="minutes")
    history, change = changes.record(_read_json(out / "changes.json", []), _read_json(out / "csi_decisions.json", None),
                                     export, now)
    m["changes"], m["change_new"] = history, change
    topic_dir = out / "by_topic"
    if topic_dir.exists():
        shutil.rmtree(topic_dir)  # 주제 id를 바꾸면 옛 파일이 남지 않도록
    topic_dir.mkdir(parents=True)
    (out / "index.html").write_text(render_html.render_html(m), encoding="utf-8")
    (out / "README.md").write_text(render_md.readme(m), encoding="utf-8")
    for t in m["topics"]:
        (topic_dir / f"{t['id']}.md").write_text(render_md.topic_page(m, t), encoding="utf-8")
    (out / "csi_decisions.json").write_text(json.dumps(export, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (out / "changes.json").write_text(json.dumps(history, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    if notify_file and change and (config.get("notify") or {}).get("issue", True):
        Path(notify_file).write_text(render_md.notification(m, change), encoding="utf-8")
    return m


def summary(m):
    conf = [e for e in m["entries"] if model.confirmed(e)]
    lines = [f"원본 DB 업데이트: {m['updated_kst']} · 회의 {m['meetings'][0]} – {m['latest']} ({len(m['meetings'])}회)",
             f"확정 {len(conf)}건 (Agreement {sum(1 for e in conf if model.agreement(e))}) · 후보 {len(m['entries']) - len(conf)}건"]
    for t in m["topics"]:
        lines.append(f"  - {t['label']}: 확정 {sum(1 for e in conf if e['topic'] == t['id'])}"
                     f" (관련 포함 {sum(1 for e in conf if t['id'] in e['tags'])})")
    for a in m["agendas"]:
        if not a["entries"]:
            lines.append(f"::warning::포함 Agenda '{a['label']}'에 맞는 결정이 없습니다. 제목이 바뀌었는지 확인하세요.")
    for d in m["alerts"]["dropped"]:
        lines.append(f"::warning::포함 Agenda '{d['label']}'가 {m['prev']}에는 {d['prev_count']}건 있었지만 {m['latest']}에는 없습니다."
                     " 제목·섹션이 바뀌었으면 config agendas를 고치세요.")
    for r in m["alerts"]["new"]:
        lines.append(f"::warning::{m['latest']}에 새 Agenda '{r['number']} {r['title']}' ({r['section']}): "
                     f"확정 {r['confirmed']} · 후보 {r['candidate']}건. CSI Agenda면 config agendas에 넣으세요.")
    c = m["change_new"]
    if c:
        lines.append(f"변경 이력 추가 ({c['reason']}): 새 회의 " + (", ".join(f"{x['meeting']} {x['count']}건" for x in c["new_meetings"]) or "없음")
                     + f" · 기존 회의 추가 {c['counts']['added']} · 변경 {c['counts']['changed']} · 삭제 {c['counts']['removed']}")
    else:
        lines.append("변경 없음 (직전 결과와 같음)")
    if m["unknown_manual_ids"]:
        lines.append("::warning::원본 DB에 없는 수동 목록 id: " + ", ".join(m["unknown_manual_ids"]))
    for p in m["provisional"]:
        lines.append(f"{p}: 잠정 결과 (회의 종료본 전)")
    return "\n".join(lines)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--db", help="원본 DB 파일 (없으면 config의 원본 저장소에서 받음)")
    ap.add_argument("--config", default=str(ROOT / "config" / "csi_scope.yaml"))
    ap.add_argument("--out", default=str(ROOT / "reports"))
    ap.add_argument("--notify-file", help="변경이 있으면 알림(GitHub Issue) 본문을 쓸 파일")
    args = ap.parse_args(argv)
    config = load_config(args.config)
    db = source.load(config, args.db)
    print(summary(build(config, db, args.out, notify_file=args.notify_file)))


if __name__ == "__main__":
    main()
