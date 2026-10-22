"""생성한 대시보드를 실제 브라우저(Chromium)로 열어 화면 동작을 확인합니다.

playwright가 없으면 건너뜁니다. CI에서는 REQUIRE_BROWSER_TEST=1로 실행해 건너뛰지 않고 실패하게 합니다.
"""
import csv
import io
import os
import re
from urllib.parse import quote

import pytest

from scripts import build

if os.environ.get("REQUIRE_BROWSER_TEST") != "1":
    pytest.importorskip("playwright.sync_api")
from playwright.sync_api import sync_playwright  # noqa: E402


@pytest.fixture
def dash(tmp_path, db, config):
    yield from _open(tmp_path, db, config)


@pytest.fixture
def dash_many(tmp_path, db, config):
    # 한 화면(20건)보다 많은 결정: #125 Beam management 결정을 원문만 바꿔 25건 더함
    base = next(e for e in db["entries"] if e["id"] == "RAN1#125:10.5.2.4:001")
    extra = [{**base, "id": f"RAN1#125:10.5.2.4:{i:03d}", "text": f"- Support option {i} for beam reporting."} for i in range(2, 27)]
    db = {**db, "entries": db["entries"] + extra}
    yield from _open(tmp_path, db, config)


def _open(tmp_path, db, config):
    build.build(config, db, tmp_path)
    errors = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        pg = browser.new_page(viewport={"width": 1280, "height": 900})
        pg.on("pageerror", lambda e: errors.append(str(e)))
        pg.route(re.compile(r"fonts\.(googleapis|gstatic)\.com"), lambda r: r.abort())  # 외부 글꼴 없이도 동작해야 함
        pg.goto((tmp_path / "index.html").as_uri())
        pg.wait_for_selector("#results .result", state="attached")  # 결정 목록은 처음엔 숨겨진 탭에 있음
        yield pg
        browser.close()
    assert errors == []


def tab(pg, name):
    pg.click(f'[data-tab="{name}"]')


def count(pg):
    return int(re.match(r"(\d+)건", pg.text_content("#summary")).group(1))


def test_default_shows_confirmed_agreements(dash):
    assert dash.text_content("#state").startswith("표시 중: 확정 · Agreement")
    assert dash.is_checked('input[value="Agreement"]') and not dash.is_checked('input[value="Working Assumption"]')
    assert not dash.is_checked("#g-cand")


def test_chart_click_clears_previous_conditions(dash):
    # 이전 조건(Agenda 필터 + 검색어)이 남아 있어도 차트 조각을 누르면 그 조각의 건수가 그대로 나와야 함
    tab(dash, "agenda")
    dash.locator("#agenda-body tr", has_text="Beam management for downlink and uplink").locator("button.cell").last.click()
    assert dash.is_visible("#results")                               # 숫자를 누르면 결정 목록 탭으로
    dash.fill("#q", "zzzz")
    tab(dash, "summary")
    seg = dash.locator("svg#chart path.seg").first
    expected = int(re.search(r"(\d+)건$", seg.get_attribute("aria-label")).group(1))
    seg.click()
    assert count(dash) == expected
    assert dash.input_value("#q") == "" and dash.input_value("#f-agenda") == ""


def test_card_click_shows_latest_meeting_only(dash):
    tab(dash, "list")
    dash.fill("#q", "zzzz")
    tab(dash, "summary")
    dash.locator("#delta .card").first.click()  # '전체' 카드
    assert dash.input_value("#f-meeting") == "RAN1#126" and dash.input_value("#q") == ""
    assert count(dash) == int(dash.locator("#delta .card .big").first.text_content())


def test_related_topic_filter_includes_primary(dash):
    tab(dash, "list")
    dash.select_option("#f-topic", "p:csirs")
    primary = count(dash)
    dash.select_option("#f-topic", "t:csirs")
    assert count(dash) > primary  # 주된 주제가 CSI 보고인 'aperiodic CSI reporting … NZP CSI-RS' 결정이 더해짐
    tab(dash, "summary")
    row = dash.locator("#topic-body tr", has_text="CSI-RS")
    row.locator("td.related button").click()
    assert dash.input_value("#f-topic") == "t:csirs"


def test_candidate_keywords_are_readable(dash):
    dash.check("#g-cand")
    tab(dash, "agenda")
    dash.locator("#agenda-body tr", has_text="Uplink transmission scheme").locator("button.cell").last.click()
    kws = dash.locator(".kw").all_text_contents()
    assert kws and all("\\" not in k and "(?" not in k for k in kws)
    assert kws == ["일치: codebook, SRS"]


def test_children_agenda_number_not_shown_as_renumbered(dash):
    tab(dash, "agenda")
    row = dash.locator("#agenda-body tr", has_text="Maintenance on NR MIMO Phase N")
    assert row.locator(".sub").text_content() == "Agenda 8.2"


def test_theme_toggle(dash):
    dash.click("#theme")
    assert dash.get_attribute("html", "data-theme") == "light"
    dash.click("#theme")
    assert dash.get_attribute("html", "data-theme") == "dark"


def test_hidden_counts_are_shown_and_clickable(dash):
    state = dash.text_content("#state")
    assert "숨김:" in state and "후보" in state
    dash.locator("#state .hidden-btn", has_text="Conclusion").click()
    assert dash.is_checked('input[value="Conclusion"]')
    hidden = dash.text_content("#latest-hidden")
    assert hidden.startswith("RAN1#126에서 기본 화면(확정 Agreement) 밖에 있는 결정") and "후보" in hidden
    dash.locator("#latest-hidden .hidden-btn", has_text="후보").click()
    assert dash.is_checked("#g-cand") and dash.input_value("#f-agenda") == "cand"
    assert count(dash) == int(re.search(r"후보 (\d+)건", hidden).group(1))


def test_tables_links_and_warnings_in_decisions(dash):
    tab(dash, "list")
    dash.fill("#q", "58-3-1")
    dash.wait_for_timeout(400)  # 검색창은 입력 후 150ms 뒤에 반영
    first = dash.locator("#results .result").first
    assert first.locator(".orig-table td").count() >= 4                 # '|' 줄이 표로
    assert first.locator(".chip.stage").text_content() == "UE features (FG)"
    dash.fill("#q", "R1-2607797")
    dash.wait_for_timeout(400)
    chip = dash.locator("#results .result").first.locator(".warn-chip")
    assert chip.text_content() == "⚠ 변경은 TDoc에" and "실제 변경 내용은 TDoc에" in chip.get_attribute("title")


def test_extra_filters_ffs_and_fg_sections(dash):
    tab(dash, "list")
    dash.click("#more-filters summary")                              # 상세 필터는 접혀 있음
    dash.select_option("#f-stage", "study")
    assert "1개 적용 중" in dash.text_content("#more-state")
    n_study = count(dash)
    assert 0 < n_study and all(c == "Study" for c in dash.locator("#results .chip.stage").all_text_contents())
    dash.click("#reset")
    dash.select_option("#f-clause", "TS 38.214 5.2")
    assert count(dash) >= 1
    tab(dash, "ffs")
    assert dash.is_hidden("#filters")                                # 구분·범위 필터 줄은 FFS 탭에 적용되지 않아 숨김
    assert re.match(r"\d+줄", dash.text_content("#ffs-summary"))
    dash.locator("#ffs .link-btn").first.click()                      # '원 결정 보기' → 목록에 그 결정 1건
    assert count(dash) == 1
    tab(dash, "fg")
    assert dash.locator("#fg-body tr").count() >= 1
    dash.locator("#fg-body .link-btn").first.click()
    assert count(dash) >= 1 and "정의·수정 결정" in dash.text_content("#summary")


def test_tabs_start_on_summary_and_open_from_hash(dash):
    assert dash.is_visible("#delta") and dash.is_hidden("#results") and dash.is_hidden("#ffs-list")
    assert dash.get_attribute('[data-tab="summary"]', "aria-selected") == "true"
    tab(dash, "fg")
    assert dash.evaluate("location.hash") == "#fg" and dash.is_visible("#fg-body") and dash.is_hidden("#delta")
    dash.goto(dash.url.split("#")[0] + "#ffs")                         # 공유한 주소의 #탭으로 바로 열림
    dash.wait_for_timeout(200)
    assert dash.is_visible("#ffs-list") and dash.is_hidden("#filters")


def test_first_visit_guide(tmp_path, db, config):
    # localStorage는 file:// 주소에서 브라우저마다 다르게 동작하므로(실제 게시 주소는 https) 로컬 HTTP 서버로 엽니다.
    import functools
    import threading
    from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

    build.build(config, db, tmp_path)
    handler = functools.partial(SimpleHTTPRequestHandler, directory=str(tmp_path))
    handler.log_message = lambda *a: None
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            pg = browser.new_page()
            pg.route(re.compile(r"fonts\.(googleapis|gstatic)\.com"), lambda r: r.abort())
            pg.goto(f"http://127.0.0.1:{server.server_address[1]}/index.html")
            assert pg.get_attribute("#guide", "open") is not None             # 처음 방문: 펼쳐짐
            pg.locator('#guide [data-goto="ffs"]').click()                     # 안내 속 탭 이름 → 그 탭으로
            assert pg.is_visible("#ffs-list")
            pg.click("#guide > summary")                                       # 접으면 기억
            pg.wait_for_function("localStorage.getItem('csi-guide-seen') === '1'")  # toggle 이벤트는 비동기
            pg.reload()
            pg.wait_for_selector("#guide", state="attached")
            assert pg.get_attribute("#guide", "open") is None
            browser.close()
    finally:
        server.shutdown()


def test_choosing_candidate_agenda_turns_on_candidates(dash):
    tab(dash, "list")
    assert not dash.is_checked("#g-cand")
    label = [o for o in dash.eval_on_selector_all("#f-agenda option", "os => os.map(o => o.textContent)") if o.startswith("[후보]")][0]
    dash.select_option("#f-agenda", label=label)
    assert dash.is_checked("#g-cand") and count(dash) >= 1


def test_copy_link_opens_only_that_decision(dash):
    tab(dash, "list")
    dash.evaluate("navigator.clipboard.writeText = t => { window.__copied = t; return Promise.resolve(); }")  # 권한 없이 확인
    card = dash.locator("#results .result").first
    rid = card.locator(".src .mono").last.text_content()
    card.get_by_role("button", name="링크 복사").click()
    assert card.get_by_role("button", name="복사됨").is_visible()
    url = dash.evaluate("window.__copied")
    assert url == dash.url.split("#")[0] + "#id=" + quote(rid, safe="")
    tab(dash, "summary")
    dash.goto(url)                                                       # 같은 페이지에서 주소만 바뀜 (hashchange)
    assert dash.is_visible("#results") and count(dash) == 1 and "공유된 결정" in dash.text_content("#summary")
    assert dash.locator("#results .result .src .mono").last.text_content() == rid
    dash.reload()                                                        # 처음 여는 경우
    dash.wait_for_selector("#results .result")
    assert count(dash) == 1 and dash.evaluate("location.hash") == "#id=" + quote(rid, safe="")


def test_shared_link_with_renumbered_id_shows_same_agenda(dash):
    dash.goto(dash.url.split("#")[0] + "#id=" + quote("RAN1#126:10.5.3.4:099", safe=""))
    dash.wait_for_timeout(200)
    assert count(dash) == 1 and "같은 회의·Agenda(RAN1#126 10.5.3.4)" in dash.text_content("#summary")


def test_csv_download_has_all_hits(dash_many, db):
    dash = dash_many
    tab(dash, "list")
    n = count(dash)
    assert n > dash.locator("#results .result").count() and dash.text_content("#csv") == f"CSV 내려받기 ({n}건)"     # '더 보기' 전 20건이 아니라 전부
    with dash.expect_download() as d:
        dash.click("#csv")
    raw = open(d.value.path(), "rb").read()
    assert raw.startswith(b"\xef\xbb\xbf")                                        # 엑셀용 UTF-8 BOM
    rows = list(csv.reader(io.StringIO(raw.decode("utf-8-sig"), newline="")))
    head, body = rows[0], rows[1:]
    assert head[:3] == ["id", "회의", "신규"] and head[-3:] == ["담당자", "반영 여부", "메모"]
    assert len(body) == n
    text = {e["id"]: e["text"] for e in db["entries"]}
    col = head.index("Chair notes 원문")
    for r in body:
        orig = text.get(r[0], f"- Support option {int(r[0][-3:])} for beam reporting.")
        assert r[col] == ("'" + orig if orig[:1] in "=+-@" else orig)               # 원문 그대로 (수식 방지 ' 만)
    assert any(r[col].startswith("'- Support option") for r in body)
    assert body[0][head.index("대시보드 링크")].endswith("#id=" + quote(body[0][0], safe=""))
    dash.fill("#q", "zzzz")
    dash.wait_for_timeout(400)
    assert dash.is_disabled("#csv")


def test_source_line_shows_tdoc_or_why_not(dash):
    tab(dash, "list")
    srcs = dash.locator("#results .result .src")
    texts = srcs.all_text_contents()
    assert all("회의록" in x and "근거 TDoc" in x for x in texts)
    with_tdoc = dash.locator("#results .result .src a.mono").first           # 합성 DB의 근거 TDoc
    assert with_tdoc.text_content() == "R1-2600001" and with_tdoc.get_attribute("href").endswith("R1-2600001.zip")
