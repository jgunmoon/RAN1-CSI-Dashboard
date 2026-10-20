"""생성한 대시보드를 실제 브라우저(Chromium)로 열어 화면 동작을 확인합니다.

playwright가 없으면 건너뜁니다. CI에서는 REQUIRE_BROWSER_TEST=1로 실행해 건너뛰지 않고 실패하게 합니다.
"""
import os
import re

import pytest

from scripts import build

if os.environ.get("REQUIRE_BROWSER_TEST") != "1":
    pytest.importorskip("playwright.sync_api")
from playwright.sync_api import sync_playwright  # noqa: E402


@pytest.fixture
def dash(tmp_path, db, config):
    build.build(config, db, tmp_path)
    errors = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        pg = browser.new_page(viewport={"width": 1280, "height": 900})
        pg.on("pageerror", lambda e: errors.append(str(e)))
        pg.route(re.compile(r"fonts\.(googleapis|gstatic)\.com"), lambda r: r.abort())  # 외부 글꼴 없이도 동작해야 함
        pg.goto((tmp_path / "index.html").as_uri())
        pg.wait_for_selector("#results .result")
        yield pg
        browser.close()
    assert errors == []


def count(pg):
    return int(re.match(r"(\d+)건", pg.text_content("#summary")).group(1))


def test_default_shows_confirmed_agreements(dash):
    assert dash.text_content("#state").startswith("표시 중: 확정 · Agreement")
    assert dash.is_checked('input[value="Agreement"]') and not dash.is_checked('input[value="Working Assumption"]')
    assert not dash.is_checked("#g-cand")


def test_chart_click_clears_previous_conditions(dash):
    # 이전 조건(Agenda 필터 + 검색어)이 남아 있어도 차트 조각을 누르면 그 조각의 건수가 그대로 나와야 함
    dash.locator("#agenda-body tr", has_text="Beam management for downlink and uplink").locator("button.cell").last.click()
    dash.fill("#q", "zzzz")
    seg = dash.locator("svg#chart path.seg").first
    expected = int(re.search(r"(\d+)건$", seg.get_attribute("aria-label")).group(1))
    seg.click()
    assert count(dash) == expected
    assert dash.input_value("#q") == "" and dash.input_value("#f-agenda") == ""


def test_card_click_shows_latest_meeting_only(dash):
    dash.fill("#q", "zzzz")
    dash.locator("#delta .card").first.click()  # '전체' 카드
    assert dash.input_value("#f-meeting") == "RAN1#126" and dash.input_value("#q") == ""
    assert count(dash) == int(dash.locator("#delta .card .big").first.text_content())


def test_related_topic_filter_includes_primary(dash):
    dash.select_option("#f-topic", "p:csirs")
    primary = count(dash)
    dash.select_option("#f-topic", "t:csirs")
    assert count(dash) > primary  # 주된 주제가 CSI 보고인 'aperiodic CSI reporting … NZP CSI-RS' 결정이 더해짐
    row = dash.locator("#topic-body tr", has_text="CSI-RS")
    row.locator("td.related button").click()
    assert dash.input_value("#f-topic") == "t:csirs"


def test_candidate_keywords_are_readable(dash):
    dash.check("#g-cand")
    dash.locator("#agenda-body tr", has_text="Maintenance on AI/ML for NR Air interface").locator("button.cell").last.click()
    kws = dash.locator(".kw").all_text_contents()
    assert kws and all("\\" not in k and "(?" not in k for k in kws)
    assert any("TS 38.214 5.2.2.5" in k for k in kws)


def test_children_agenda_number_not_shown_as_renumbered(dash):
    row = dash.locator("#agenda-body tr", has_text="Maintenance on NR MIMO Phase 5")
    assert row.locator(".sub").text_content() == "Agenda 8.2"


def test_theme_toggle(dash):
    dash.click("#theme")
    assert dash.get_attribute("html", "data-theme") == "light"
    dash.click("#theme")
    assert dash.get_attribute("html", "data-theme") == "dark"
