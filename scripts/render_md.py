"""마크다운 리포트: reports/README.md(요약 대시보드)와 reports/by_topic/<주제>.md(주제별 전체 결정)."""
from scripts.model import (SCOPE_LABEL, TYPE_SHORT, TYPES, agreement, candidate_agendas, confirmed, count, provisional,
                           short)


def _cell(text):
    return str(text).replace("|", "\\|").replace("\n", " ")


def _first_line(text, n=110):
    line = text.strip().split("\n")[0].strip()
    return line if len(line) <= n else line[:n - 1] + "…"


def _source(s):
    parts = [f"[{s['doc']}]({s['url']})"]
    if s.get("tdoc"):
        parts.append(f"[{s['tdoc']}]({s['tdoc_url']})" if s.get("tdoc_url") else s["tdoc"])
    if s.get("discussion"):
        parts.append(f"`[{s['discussion']}]`")
    return " · ".join(parts)


def _matrix(rows, meetings, header):
    head = f"| {header} | " + " | ".join(short(m) for m in meetings) + " | 합계 |"
    out = [head, "|" + "---|" * 1 + "---:|" * (len(meetings) + 1)]
    totals = dict.fromkeys(meetings, 0)
    for label, per in rows:
        for m in meetings:
            totals[m] += per.get(m, 0)
        out.append(f"| {_cell(label)} | " + " | ".join(str(per.get(m, 0) or "·") for m in meetings)
                   + f" | **{sum(per.values())}** |")
    out.append("| **합계** | " + " | ".join(f"**{totals[m]}**" for m in meetings) + f" | **{sum(totals.values())}** |")
    return "\n".join(out)


def topic_slug(topic_id):
    return f"by_topic/{topic_id}.md"


def readme(m):
    cfg, db, meetings, entries = m["config"], m["db"], m["meetings"], m["entries"]
    latest, prev = m["latest"], m["prev"]
    conf = [e for e in entries if confirmed(e)]
    cand = [e for e in entries if not confirmed(e)]
    by_type = {t: sum(1 for e in conf if e["type"] == t) for t in TYPES}
    out = ["# RAN1 CSI 결정 대시보드", "",
           f"> 원본 DB 마지막 업데이트 **{m['updated_kst'] or '기록 없음'}** · "
           f"범위 {meetings[0]} – {short(latest)} ({len(meetings)}회) · "
           f"[HTML 대시보드]({cfg.get('dashboard_url', 'index.html')}) · 원본 [{cfg['source']['repo']}](https://github.com/{cfg['source']['repo']})",
           ""]
    for p in m["provisional"]:
        out += [f"> ⚠️ **{p}는 '잠정'** 결과입니다 (`{provisional(db, p)['doc']}` 기준, 회의 종료본 전). 결정이 바뀌거나 빠질 수 있습니다.", ""]
    out += ["3GPP RAN1 Chair notes의 결정 중 CSI 관련(CSI 획득·보고, CSI-RS, codebook, beam management, SRS, AI/ML CSI)만 모았습니다.",
            "범위·주제 규칙은 [`config/csi_scope.yaml`](../config/csi_scope.yaml)에 있습니다. 이 파일은 자동 생성물이므로 직접 고치지 않습니다.", "",
            "| 구분 | 건수 |", "|---|---:|",
            f"| 확정 (포함 Agenda + 수동 포함) | **{len(conf)}** (Agreement {by_type['Agreement']} · WA {by_type['Working Assumption']} · Conclusion {by_type['Conclusion']}) |",
            f"| 후보 (다른 Agenda의 키워드 일치, 확인 필요) | {len(cand)} |", ""]

    topics = m["topics"]
    agr = count(conf, lambda e: e["topic"], meetings, agreement)
    if prev:
        out += [f"## 직전 회의 대비 ({prev} → {latest})", "",
                f"확정 범위의 Agreement 수입니다. {latest}의 결정은 모두 이번 회의의 신규 결정입니다.", "",
                f"| 주제 | {short(prev)} | **{short(latest)}** | 증감 |", "|---|---:|---:|---:|"]
        for t in topics:
            a, b = agr[t["id"]][prev], agr[t["id"]][latest]
            out.append(f"| [{t['label']}]({topic_slug(t['id'])}) | {a} | **{b}** | {b - a:+d} |")
        a, b = sum(agr[t["id"]][prev] for t in topics), sum(agr[t["id"]][latest] for t in topics)
        out += [f"| **합계** | {a} | **{b}** | {b - a:+d} |", ""]

    out += ["## 주제별 · 회의별 Agreement", "",
            "확정 범위의 Agreement만 셉니다. Working Assumption·Conclusion과 후보는 HTML 대시보드에서 체크박스로 켤 수 있습니다.", "",
            _matrix([(f"[{t['label']}]({topic_slug(t['id'])})", agr[t["id"]]) for t in topics], meetings, "주제"), ""]
    per_meeting = [sum(agr[t["id"]][mt] for t in topics) for mt in meetings]
    out += ["```mermaid", "xychart-beta", '    title "회의별 CSI Agreement (확정 범위)"',
            "    x-axis [" + ", ".join(f'"{short(mt)}"' for mt in meetings) + "]",
            f'    y-axis "건수" 0 --> {max(per_meeting + [1]) + 5}',
            "    bar [" + ", ".join(str(n) for n in per_meeting) + "]", "```", ""]

    rows = []
    for a in m["agendas"]:
        per = dict.fromkeys(meetings, 0)
        for e in a["entries"]:
            if agreement(e):
                per[e["meeting"]] += 1
        rows.append((f"{a['label']} ({a['section']}, 최근 {a['last_number'] or '-'})", per))
    manual = [e for e in conf if e["scope"] == "manual"]
    if manual:
        per = dict.fromkeys(meetings, 0)
        for e in manual:
            if agreement(e):
                per[e["meeting"]] += 1
        rows.append(("수동 포함 (include_ids)", per))
    out += ["## 포함 Agenda별 · 회의별 Agreement", "",
            "Agenda 번호는 회의마다 바뀌므로 '섹션 + Agenda 제목'으로 이어 붙였습니다. 괄호 안 번호는 가장 최근 회의 번호입니다.", "",
            _matrix(rows, meetings, "Agenda"), ""]

    new = [e for e in conf if e["meeting"] == latest and agreement(e)]
    out += [f"## {latest} 신규 CSI Agreement ({len(new)}건)", "",
            "아래 문장은 요약이 아니라 **원문 첫 줄**입니다(길면 자름). 전체 원문은 주제별 리포트와 HTML 대시보드에 있습니다.", "",
            "| 주제 | Agenda | 원문 첫 줄 | 출처 |", "|---|---|---|---|"]
    for e in new:
        out.append(f"| {m['topic_label'][e['topic']]} | {e['agenda_item']} {_cell(e['agenda_title'])} | "
                   f"{_cell(_first_line(e['text']))} | {_source(e['source'])} |")
    out.append("")

    out += ["## 후보가 많은 Agenda", "",
            "포함 Agenda 밖에서 보조 키워드로 잡힌 결정입니다. CSI 관련이 맞으면 결정 id를 `include_ids`에, 아니면 `exclude_ids`에 적습니다.", "",
            "| 섹션 | Agenda | 번호 | 후보 수 |", "|---|---|---|---:|"]
    for s, t, n, nums in candidate_agendas(m)[:15]:
        out.append(f"| {_cell(s)} | {_cell(t)} | {', '.join(nums)} | {n} |")
    if m["unknown_manual_ids"]:
        out += ["", "> ⚠️ 원본 DB에 없는 수동 목록 id: " + ", ".join(f"`{i}`" for i in m["unknown_manual_ids"])]
    out += ["", "---", "모든 결정은 3GPP FTP의 Chair notes 원문 그대로이며, 각 결정 끝에 Chair notes와 근거 TDoc 링크를 붙였습니다.",
            "이 리포트는 `python -m scripts.build`가 자동으로 생성합니다.", ""]
    return "\n".join(out)


def _entry_md(e, m):
    meta = [f"**{TYPE_SHORT[e['type']]}**", f"`{e['agenda_item']}` {e['agenda_title']}", f"`{e['id']}`"]
    if e["scope"] != "agenda":
        meta.append(SCOPE_LABEL[e["scope"]])
    if e["meeting"] == m["latest"]:
        meta.append("🆕 신규")
    lines = [" · ".join(meta), ""]
    lines += ["> " + ln if ln.strip() else ">" for ln in e["text"].split("\n")]
    if e.get("ffs"):
        lines += ["", f"남은 FFS {len(e['ffs'])}건"]
    lines += ["", f"출처: {_source(e['source'])}", ""]
    return lines


def topic_page(m, topic):
    tid = topic["id"]
    mine = [e for e in m["entries"] if e["topic"] == tid]
    conf = [e for e in mine if confirmed(e)]
    cand = [e for e in mine if not confirmed(e)]
    out = [f"# {topic['label']} — RAN1 CSI 결정", "",
           f"> 원본 DB 마지막 업데이트 **{m['updated_kst'] or '기록 없음'}** · [요약으로 돌아가기](../README.md)", "",
           f"확정 {len(conf)}건 (" + " · ".join(f"{TYPE_SHORT[t]} {sum(1 for e in conf if e['type'] == t)}" for t in TYPES)
           + f"), 후보 {len(cand)}건. 결정 본문은 Chair notes 원문 그대로입니다(요약 없음). 최신 회의부터 보여줍니다.", ""]
    for mt in reversed(m["meetings"]):
        here = [e for e in conf if e["meeting"] == mt]
        if not here:
            continue
        flag = " (잠정)" if mt in m["provisional"] else ""
        out += [f"## {mt}{flag} — {len(here)}건", ""]
        for e in here:
            out += _entry_md(e, m)
    if cand:
        out += ["---", "", f"## 후보 {len(cand)}건 (키워드 일치 · 확인 필요)", "",
                "포함 Agenda 밖에서 키워드로 잡힌 결정입니다. CSI 범위가 아닐 수 있습니다.", ""]
        for mt in reversed(m["meetings"]):
            here = [e for e in cand if e["meeting"] == mt]
            if here:
                out += [f"### {mt} — {len(here)}건", ""]
                for e in here:
                    out += _entry_md(e, m)
    return "\n".join(out)
