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
   - `candidate_keywords`: 포함 Agenda 밖에서 키워드가 원문/FFS에 있으면 **'후보'**. 확정과 섞지 않고 따로 표시합니다.
     `ignore_phrases`(예: HARQ-ACK codebook)는 판정 전에 지웁니다.
   - `include_ids` / `exclude_ids`: 결정 id로 사람이 확정하거나 뺍니다.
   - `topics`: 결정마다 주제 하나. Agenda 고정 주제 → 없으면 규칙을 위에서부터 보고 처음 맞는 것 → 없으면 `fallback_topic`.
   범위를 바꿀 때는 먼저 원본 DB로 건수를 확인하고(아래 명령의 출력) 사용자 확인을 받습니다.
4. **기본 표시는 확정 범위의 Agreement.** Working Assumption·Conclusion, 'FFS 남은 결정만', 후보는 체크박스로 켭니다.
5. **'잠정' 회의.** 원본 DB의 `meetings.*.provisional`이 있는 회의는 종료본 전 결과이므로 README·대시보드에 '잠정'으로 표시합니다.

## 2. 구조

```text
config/csi_scope.yaml        # 원본 DB 위치(저장소·브랜치), 포함 Agenda, 키워드, 수동 목록, 주제 규칙, 추천 검색어
scripts/source.py            # 원본 DB 읽기 + 스키마 검사 (raw.githubusercontent.com/<repo>/<branch>/<db_path>)
scripts/scope.py             # 범위 판정(agenda/manual/candidate)과 주제 분류
scripts/model.py             # 리포트용 집계 (HTML·마크다운 공용)
scripts/render_html.py       # reports/index.html (HTML 대시보드)
scripts/render_md.py         # reports/README.md(요약), reports/by_topic/<주제>.md(주제별 전체 결정)
scripts/build.py             # 진입점: 원본 DB → reports/ 전체 생성
reports/                     # 생성물 (직접 수정 금지). csi_decisions.json은 고른 결정 + 주제·범위
tests/                       # 합성 DB로 범위 판정·리포트 생성 테스트
.github/workflows/csi_dashboard.yml   # 매일 01:17 UTC 실행 → reports/ 커밋 → GitHub Pages 게시
```

## 3. 명령

```bash
pip install -r requirements.txt
python -m pytest -q
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
- 차트 주제 색은 config `topics` 순서대로 dataviz 기본 범주 팔레트 1~5번을 쓰고, 마지막(기타)은 회색입니다. 주제를 6개 넘게 늘리면 색 규칙을 다시 정합니다.
- `reports/` 아래 파일은 생성물입니다. 직접 고치지 말고 설정이나 스크립트를 고친 뒤 다시 생성합니다.
