import json, sys, glob, os
from jsonschema import Draft202012Validator

# ここを content/quizzes に変更
SCHEMA_PATH = os.path.join("content", "quizzes", "schema.json")

with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
    schema = json.load(f)

validator = Draft202012Validator(schema)

for path in glob.glob(os.path.join("content", "quizzes", "*.json")):
    # ダッシュボード用のインデックスはスキップ
    if os.path.basename(path) in ("index.json", "schema.json"):
        continue
    with open(path, "r", encoding="utf-8") as f:
        try:
            items = json.load(f)
        except Exception as e:
            print(f"{path}: JSON 読み込み失敗: {e}")
            sys.exit(1)

    if not isinstance(items, list):
        print(f"{path}: ルートは配列であるべきです")
        sys.exit(1)

    for idx, q in enumerate(items):
        for e in validator.iter_errors(q):
            print(f"{path}[{idx}]: {e.message}")
            sys.exit(1)

        if q.get("question_type") == "journal_input":
            ans = q.get("answer", [])
            dr = sum(x.get("amount",0) for x in ans if x.get("side")=="Dr")
            cr = sum(x.get("amount",0) for x in ans if x.get("side")=="Cr")
            if dr != cr:
                print(f"{path}[{idx}]: 借方{dr}と貸方{cr}が不一致")
                sys.exit(1)

print("OK: quizzes validated")
