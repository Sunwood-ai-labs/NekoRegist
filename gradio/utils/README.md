# ユーティリティ関数

## 概要
このディレクトリには、アプリケーション全体で使用される共通のユーティリティ関数が含まれています。

## モジュール一覧

### db.py
データベース操作のための関数群

#### 主な関数
- `init_db()`: データベース接続の初期化
- `add_cat()`: 猫の情報をデータベースに追加
- `get_all_cats()`: 登録済みの猫一覧を取得

### s3.py
AWS S3操作のための関数群

#### 主な関数
- `upload_image()`: 画像をS3にアップロード
- `get_image_url()`: アップロードされた画像のURLを取得

## 使用方法
```python
from utils.db import init_db, add_cat
from utils.s3 import upload_image

# データベース初期化
init_db()

# 画像アップロード
image_url = upload_image(image_data, "cats/example.jpg")

# データベースに保存
cat_id = add_cat("タマ", 3, "雑種", image_url)
```

## 開発ガイドライン
1. 新しいユーティリティ関数は適切なモジュールに追加
2. 共通で使用される関数のみをここに配置
3. モジュール固有の関数は各モジュールに配置
4. すべての関数に適切なドキュメント文字列を追加
