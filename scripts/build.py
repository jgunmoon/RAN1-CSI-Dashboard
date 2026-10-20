"""원본 DB를 읽어 CSI 리포트를 만듭니다 (자동 실행 진입점).

    python -m scripts.build                    # config의 원본 저장소에서 DB를 받아 reports/ 생성
    python -m scripts.build --db 파일.json     # 내려받은 DB 파일로 생성 (오프라인·테스트)

reports/index.html(HTML 대시보드), reports/README.md(요약), reports/by_topic/*.md(주제별 전체 결정),
reports/csi_decisions.json(고른 결정과 주제·범위 표시)을 만듭니다. 같은 DB와 설정이면 같은 결과가 나옵니다.
"""
import argparse
import json
import shutil
from pathlib import Path

import yaml

from scripts import model, render_html, render_md, source

ROOT = Path(__file__).resolve().parent.parent


def load_config(path=ROOT / "config" / "csi_scope.yaml"):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def build(config, db, out_dir):
    m = model.build(db, config)
    if not m["meetings"]:
        raise ValueError("원본 DB에 회의가 없습니다")
    out = Path(out_dir)
    topic_dir = out / "by_topic"
    if topic_dir.exists():
        shutil.rmtree(topic_dir)  # 주제 id를 바꾸면 옛 파일이 남지 않도록
    topic_dir.mkdir(parents=True)
    (out / "index.html").write_text(render_html.render_html(m), encoding="utf-8")
    (out / "README.md").write_text(render_md.readme(m), encoding="utf-8")
    for t in m["topics"]:
        (topic_dir / f"{t['id']}.md").write_text(render_md.topic_page(m, t), encoding="utf-8")
    keep = ("id", "meeting", "agenda_item", "agenda_title", "agenda_path", "type", "text", "ffs", "source",
            "scope", "topic", "tags", "keywords")
    export = {"source_db": source.db_url(config), "source_updated_at": db.get("updated_at"), "topics": m["topics"],
              "entries": [{k: e.get(k) for k in keep} for e in m["entries"]]}
    (out / "csi_decisions.json").write_text(json.dumps(export, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
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
    args = ap.parse_args(argv)
    config = load_config(args.config)
    db = source.load(config, args.db)
    print(summary(build(config, db, args.out)))


if __name__ == "__main__":
    main()
