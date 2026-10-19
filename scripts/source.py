"""원본 저장소의 DB(agreements_db.json)를 읽습니다. 원본은 읽기만 하고 고치지 않습니다."""
import json
import urllib.request
from urllib.parse import quote

RAW = "https://raw.githubusercontent.com/{repo}/{branch}/{path}"
REQUIRED = ("id", "meeting", "agenda_item", "agenda_title", "agenda_path", "type", "text", "source")


def db_url(config):
    s = config["source"]
    return RAW.format(repo=s["repo"], branch=quote(s["branch"], safe=""), path=s["db_path"])


def load(config, path=None, timeout=60):
    """path가 있으면 그 파일을, 없으면 config의 원본 저장소 주소에서 DB를 읽어 검사한 뒤 돌려줍니다."""
    if path:
        with open(path, encoding="utf-8") as f:
            db = json.load(f)
    else:
        req = urllib.request.Request(db_url(config), headers={"User-Agent": "ran1-csi-dashboard"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            db = json.loads(r.read().decode("utf-8"))
    check(db)
    return db


def check(db):
    if db.get("schema_version") != 1:
        raise ValueError(f"원본 DB schema_version이 1이 아닙니다: {db.get('schema_version')!r} (스키마 변경 확인 필요)")
    entries = db.get("entries")
    if not isinstance(entries, list) or not entries:
        raise ValueError("원본 DB에 entries가 없습니다")
    for e in entries:
        missing = [k for k in REQUIRED if k not in e]
        if missing or not e["agenda_path"] or not e["source"].get("url"):
            raise ValueError(f"원본 DB 결정 {e.get('id')!r}에 필수 필드가 없습니다: {missing or 'agenda_path/source.url'}")
