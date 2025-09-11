import json, sys, glob, os
from jsonschema import Draft202012Validator

SCHEMA_PATH = os.path.join("quizzes", "schema.json")

with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
    schema = json.load(f)

validator = Draft202012Validator(schema)

errors = []
for path in glob.glob(os.path.join("quizzes", "*.json")):
    with open(path, "r", encoding="utf-8") as f:
        try:
            items = json.load(f)
        except Exception as e:
            errors.append(f"{path}: JSON 読み込み失敗: {e}")
            continue

    if not isinstance(items, list):
        errors.append(f"{path}: ルートは配列であるべきです")
        continue

    for idx, q in enumerate(items):
        for e in validator.iter_errors(q):
            errors.append(f"{path}[{idx}]: {e.message}")

        if q.get("question_type") == "journal_input":
            ans = q.get("answer", [])
            try:
                dr = sum(x["amount"] for x in ans if x.get("side")=="Dr")
                cr = sum(x["amount"] for x in ans if x.get("side")=="Cr")
                if dr != cr:
                    errors.append(f"{path}[{idx}]: 借方{dr}と貸方{cr}が不一致")
            except Exception as e:
                errors.append(f"{path}[{idx}]: 借貸検査中にエラー: {e}")

if errors:
    print("\n".join(errors))
    sys.exit(1)

print("OK: quizzes validated")
