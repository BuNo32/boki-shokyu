# 簿記初級ラボ（オフライン対応）

オフラインで配布できる静的サイト教材（MkDocs + Material）。  
解説と章末クイズ（JSON）で学びます。

## セットアップ
```bash
python3 -m venv .venv && . .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
mkdocs build     # site/ に出力
mkdocs serve     # http://127.0.0.1:8000
python scripts/validate_quizzes.py  # 問題データ検証
