# RAN1 CSI 결정 대시보드 — 에이전트 지침

3GPP RAN1 회의 결정 중 **CSI 관련**만 모아 팀이 한눈에 보는 대시보드입니다.
CSI 범위는 넓게 봅니다: CSI 획득·보고, CSI-RS, codebook(PMI/CQI/RI), beamforming, beam management(TCI, beam failure 등), SRS, AI/ML CSI(압축·예측).
사용자는 한국어를 쓰며, 대시보드·문서도 한국어로 작성합니다.

## 1. 핵심 원칙

1. **수집·파싱은 하지 않습니다.** 공개 프로젝트 `jgunmoon/RAN1-Decision-Tracker`가 3GPP FTP의 Chair notes에서 모든 결정을 매일 추출해
   `data/agreements_db.json`으로 공개합니다. 이 프로젝트는 그 DB를 **읽기만** 하며, 원본 저장소는 수정하지 않습니다.
   스키마: 원본 저장소의 `data/SCHEMA.md` (`schema_version` 1). 버전이 바뀌면 `scripts/source.py`가 실패하므로 스키마를 확인하고 고칩니다.
2. **원문 그대로, 출처 필수.** 결정 본문은 Chair notes 원문(`text`)을 그대로 보여주고, 모든 결정에 Chair notes와 근거 TDoc 링크를 붙입니다.
   이 프로젝트가 붙이는 것(주제, 신규, 후보 표시)은 원문과 구분해 표시합니다. 원문을 바꾸거나 추측으로 요약하지 않습니다.
3. **범위와 주제는 코드가 아니라 `config/csi_scope.yaml`.** Agenda 이름만으로는 섞이므로(예: 6GR Multi-antenna 아래 HARQ, PRACH) 세 층으로 정합니다.
   - `agendas`: 포함 Agenda (확정). 번호는 회의마다 바뀌므로 **'섹션 제목 + Agenda 제목'**으로 매칭합니다 (원본 `scripts/agenda.py`와 같은 정규화).
     `path`는 섹션 아래 이어진 제목 경로(중간부터 가능), `children: true`면 하위 Agenda 포함, `topic`이 있으면 주제 고정.
     제목이 `re:`로 시작하면 정규식(대소문자 무시, 전체 일치)입니다. 다음 Phase·Release Agenda를 미리 잡을 때 씁니다
     (예: `re:UE features for NR MIMO Phase \d+`).
     CSI와 다른 주제가 섞인 Agenda는 `exclude`(원문 정규식, 예: AI/ML의 positioning)로 빼거나, `require_keywords: true`로
     보조 키워드·조항이 있는 결정만 확정합니다(#125 이후 AI/ML·MIMO Ph5·NES·NTN 통합 유지보수). 빠진 결정도 키워드가 있으면 후보가 됩니다.
   - `candidate_keywords`: 포함 Agenda 밖에서 키워드가 원문/FFS에 있으면 **'후보'**. 확정과 섞지 않고 따로 표시합니다.
     `ignore_phrases`(예: HARQ-ACK codebook)는 판정 전에 지웁니다. 대시보드의 '일치'에는 정규식이 아니라 실제로 일치한 단어를 보여줍니다.
   - `spec_clauses`: 사양 조항 번호(예: TS 38.214 5.2 = CSI 보고)도 후보 키워드로 씁니다. 유지보수 결정은 "TS 38.214 Clause 5.2.5의 TP endorsed"처럼
     기술 키워드 없이 조항만 나오기 때문입니다. 같은 줄의 사양·조항을 짝짓고(`scope.clause_mentions`), 'Section 2 of R1-…' 같은 TDoc 절은 뺍니다.
     원문이 조항을 다른 사양에 잘못 붙이는 경우가 있어(예: '38.213 6.3.2.x'는 실제 38.212) 필요하면 `exact: true`로 하위 조항을 막습니다.
     #125부터 Rel-19 MIMO Phase 5·AI/ML 유지보수가 통합 Agenda(… NR MIMO Phase 5, NES and NTN)로 옮겨져 이 키워드로 후보를 잡습니다.
   - `include_ids` / `exclude_ids`: 결정 id로 사람이 확정하거나 뺍니다.
   - `topics`: 결정마다 **주된 주제** 하나와 **관련 주제** 태그(`tags`, 주된 주제 포함).
     주된 주제 = Agenda 고정 주제 → 규칙을 위에서부터 보고 처음 맞는 것 → 일치한 조항의 topic → `fallback_topic`.
     관련 주제 = 주된 주제 + 맞는 모든 규칙 + 일치한 조항의 topic. 차트·표의 회의별 숫자는 주된 주제(합계 = 전체),
     표의 '관련 포함' 열과 목록의 '관련 주제 포함' 필터는 태그로 셉니다. 'CSI 보고' 규칙의 `\bCSI\b` 패턴은 넓어서 이 태그가 많이 붙습니다.
   범위를 바꿀 때는 먼저 원본 DB로 건수를 확인하고(아래 명령의 출력) 사용자 확인을 받습니다.
4. **기본 표시는 확정 범위의 Agreement.** Working Assumption·Conclusion, 'FFS 있는 결정만', 후보는 체크박스로 켭니다.
   대신 놓치지 않도록 상태 줄에 '숨김: WA n · Conclusion n · 후보 n'(누르면 켜짐)과, 최신 회의의 기본 화면 밖 건수를 항상 보여줍니다.
5. **'잠정' 회의.** 원본 DB의 `meetings.*.provisional`이 있는 회의는 종료본 전 결과이므로 README·대시보드에 '잠정'으로 표시합니다.
6. **조용히 빠지는 것을 막는 장치.** 이 프로젝트의 목적은 CSI 담당 엔지니어가 결정을 놓치지 않는 것입니다.
   - Agenda 경고(`model.agenda_alerts`): 직전 회의에 결정이 있던 포함 Agenda가 최신 회의에 없거나, CSI 결정(확정·후보)이 있는 새 Agenda가
     생기면 대시보드·README 맨 위, 실행 요약(`::warning::`), 알림 Issue에 나옵니다. 6GR Study → WI처럼 섹션 제목이 바뀌면 여기서 잡힙니다.
     경고가 나오면 원문을 보고 `agendas`를 고칩니다(범위 변경이므로 사용자 확인). 확인했고 CSI와 무관하면(예: 6GR Modulation 이름 변경)
     config `acknowledged_alerts`에 README가 알려 주는 키('최신 회의: 섹션 > Agenda 제목' 또는 '최신 회의: 포함 Agenda 이름')를 넣어 숨깁니다.
     키에 회의가 들어 있어 다음 회의에는 다시 판단합니다. 대시보드 알림은 팀원용 문구('관리자가 확인 중')만 쓰고, 고치는 방법은 README·실행 요약·Issue에만 둡니다.
   - 변경 이력(`scripts/changes.py` → `reports/changes.json`): 매 실행 직전 `reports/csi_decisions.json`과 비교해 새 회의, 과거 회의의
     추가·변경·삭제(원본 재처리, 잠정 → 종료본, 범위 설정 변경)를 남깁니다. id만 바뀐 결정은 변경으로 보지 않습니다. 최근 30묶음 보관.
     '신규'는 최신 회의만 뜻하므로 과거 회의 변화는 이 이력과 결정 목록의 '과거 회의에 추가'/'원문 변경' 등 표시로만 보입니다.
     이유가 원본 갱신인지 설정 변경인지 구분합니다(`changes.is_source`). 결정 카드 표시와 요약 탭의 '최근 변경' 줄은 **원본(회의록) 변경만** 쓰고,
     설정 변경은 변경 이력 탭에 '대시보드 범위 조정 (RAN1 회의록 변화 아님)'으로만 남깁니다. 알림 Issue 제목도 'CSI 대시보드 범위 조정:'으로 구분합니다.
   - 알림: 결과가 달라진 실행마다 워크플로가 GitHub Issue를 만듭니다(`build --notify-file`, 첫 줄이 제목). 설정은 config `notify`.
7. **단말 알고리즘·HW 실무용 표시** (`scripts/enrich.py`, 원문은 그대로 두고 표시용 필드만 추가).
   - 진행 단계(config `stages`: UE features·유지보수 CR·Study·규격 작업), 구현 영향 태그(config `impact_tags`), 원문의 사양 조항(`clauses`).
   - ⚠ 확인 필요(`warn`): `math` 수식 누락 의심(원본 파서가 Word 수식을 못 읽어 기호가 빠진 흔적 — 근본 수정은 원본 트래커),
     `color` 색 표시 변경 손실(UE feature 표의 'chromatic fonts'), `tdoc` 실제 변경이 TDoc에만 있음.
   - 원문의 R1- 번호는 FTP 링크(`TdocLinker`): 회의 폴더를 원본 근거 TDoc 번호 범위로 추정합니다. 회의 사이 빈 구간 번호는
     인용한 결정의 회의를 우선해 실측 99%가 맞습니다(틀리면 403). 원문의 '|' 줄은 화면에서 표로 그립니다(글자는 바꾸지 않음).
   - FFS 추적: 확정 결정의 FFS 줄마다 같은 포함 Agenda 이후 회의 결정 중 단어가 많이 겹치는 것을 '후속 결정 후보'로 붙입니다.
     해소 판정이 아니며 화면에도 그렇게 적습니다. FG 목록: 확정 UE feature 표의 두 번째 칸(FG 번호)으로 FG별 정의·수정 결정을 모읍니다.

## 2. 구조

```text
config/csi_scope.yaml        # 원본 DB 위치(저장소·브랜치), 포함 Agenda, 키워드, 수동 목록, 주제 규칙, 추천 검색어
scripts/source.py            # 원본 DB 읽기 + 스키마 검사 (raw.githubusercontent.com/<repo>/<branch>/<db_path>)
scripts/scope.py             # 범위 판정(agenda/manual/candidate)과 주제 분류
scripts/model.py             # 리포트용 집계 (HTML·마크다운 공용)
scripts/render_html.py       # reports/index.html (HTML 대시보드)
scripts/render_md.py         # reports/README.md(요약), reports/by_topic/<주제>.md(주제별 전체 결정)
scripts/enrich.py            # 진행 단계·구현 영향·규격 조항·⚠ 확인 필요·TDoc 링크, FG 목록, FFS 후속 결정 후보
scripts/changes.py           # 직전 결과 대비 변경 이력 (reports/changes.json)
scripts/build.py             # 진입점: 원본 DB → reports/ 전체 생성
reports/                     # 생성물 (직접 수정 금지). csi_decisions.json은 고른 결정 + 주제·범위 (다음 실행의 비교 기준이므로 지우지 않음)
tests/                       # 합성 DB로 범위 판정·리포트 생성 테스트 + test_browser.py(Chromium으로 클릭 동작 확인)
.github/workflows/csi_dashboard.yml   # 매일 01:17 UTC 실행 → reports/ 커밋 → 변화가 있으면 알림 Issue → GitHub Pages 게시
```

## 3. 명령

```bash
pip install -r requirements.txt
python -m pytest -q                     # playwright가 없으면 화면 테스트는 건너뜀 (CI는 REQUIRE_BROWSER_TEST=1로 필수)
python -m scripts.build                 # 원본 저장소에서 DB를 받아 reports/ 생성 (요약과 경고를 출력)
python -m scripts.build --db 파일.json  # 내려받은 DB 파일로 생성
```

- 팀 공용 실행: GitHub → Actions → "RAN1 CSI dashboard" → "Run workflow". 매일 01:17 UTC(KST 10:17) 자동 실행합니다.
  원본 트래커가 23:47 UTC(KST 08:47)에 DB를 갱신하므로 그 뒤로 잡았습니다. 예약 실행은 기본 브랜치에서만 동작합니다.
- 게시 주소: https://jgunmoon.github.io/RAN1-CSI-Dashboard/ (Settings → Pages → Source: GitHub Actions 필요).
- 이 저장소(`jgunmoon/RAN1-CSI-Dashboard`)는 원본과 별개입니다. 원본 저장소에는 아무것도 푸시하지 않습니다.
  (`JG_Test_Project`는 원본 `RAN1-Decision-Tracker`의 예전 이름이므로 그 이름으로도 푸시하지 않습니다.)
- 원본 저장소의 기본 브랜치는 `ccr-0c6b397f-j6xur9`입니다. 바뀌면 `config/csi_scope.yaml`의 `source.branch`만 고칩니다.
  이 저장소의 브랜치나 주소가 바뀌면 `report_base_url`, `dashboard_url`도 고칩니다.
- 실행 요약의 `::warning::`: 포함 Agenda에 맞는 결정이 0건(제목이 바뀌었을 수 있음)이거나, 수동 목록 id가 원본 DB에 없을 때 나옵니다.
- 대시보드의 '마지막 업데이트'는 원본 DB의 `updated_at`, '마지막 확인'은 Pages 게시 단계가 `__CHECKED_AT__` 자리에 채웁니다(커밋 없음).
  자리 표시 형식을 바꾸면 워크플로도 함께 고칩니다.
- 대시보드 스크립트(`SCRIPT`)는 raw 문자열이므로 JS 문법 그대로 씁니다. 결정 데이터는 페이지 안 JSON(`#csi-data`)에 넣고 브라우저에서 집계합니다.
  화면은 탭으로 나눕니다: 요약(직전 회의 대비·최근 변경 한 줄·차트) · 결정 목록 · Agenda별 · FFS 추적 · FG 목록 · 변경 이력.
  주소의 `#탭이름`(예: `#ffs`)으로 바로 열리고, 구분·범위 필터 줄은 요약·결정 목록·Agenda별 탭에서만 보입니다.
  맨 위 '처음 보시는 분께' 안내(`_guide`)는 처음 방문 때만 펼쳐지고, 접으면 localStorage에 기억합니다. 탭·필터 이름을 바꾸면 안내 문구도 함께 고칩니다.
  긴 설명은 제목 옆 'ⓘ 설명'(`_help`)에 접어 두고, 변경 이력의 결정 목록·상세 필터도 기본으로 접습니다. 화면이 길어지지 않게 새 기능도 이 원칙을 따릅니다.
  카드·차트·표의 숫자를 누르면 `focusList`가 검색어와 다른 조건을 모두 지우고 누른 조건만 적용한 뒤 결정 목록 탭으로 갑니다(남으면 0건처럼 보임).
  주제 필터 값은 `p:<id>`(주된 주제)와 `t:<id>`(관련 주제 포함)입니다. 화면 동작을 바꾸면 tests/test_browser.py도 함께 고칩니다.
  결정 공유: 카드의 '링크 복사'는 `…/#id=<encodeURIComponent(id)>`를 복사하고, 그 주소는 결정 목록에 그 결정만 엽니다. 원본 재처리로 id 순번이
  바뀌어 없으면 같은 회의·Agenda 결정을 보여줍니다. 'CSV 내려받기'는 지금 목록의 결정 전부(UTF-8 BOM, 빈 담당자·반영 여부·메모 칸)이며,
  엑셀 수식 방지를 위해 -, =, +, @로 시작하는 칸 앞에만 `'`를 붙입니다(그 밖에는 원문 그대로). 열을 바꾸면 화면 설명과 테스트도 고칩니다.
- 화면 테스트의 playwright 버전은 requirements.txt에 고정했습니다. 클라우드 세션에는 Chromium이 미리 설치돼 있어(PLAYWRIGHT_BROWSERS_PATH)
  `playwright install` 없이 실행됩니다.
- 차트 주제 색은 config `topics` 순서대로 dataviz 기본 범주 팔레트 1~5번을 쓰고, 마지막(기타)은 회색입니다. 주제를 6개 넘게 늘리면 색 규칙을 다시 정합니다.
- `reports/` 아래 파일은 생성물입니다. 직접 고치지 말고 설정이나 스크립트를 고친 뒤 다시 생성합니다.
