# セットアップガイド

## 前提条件
- Python 3.8以上
- AWSアカウントとアクセス権限
- Terraform

## セットアップ手順

### 1. リポジトリのクローン
```bash
git clone <repository-url>
cd cat-registry
```

### 2. 環境変数の設定
以下の環境変数を設定してください：

```bash
# AWS認証情報
export AWS_ACCESS_KEY_ID="your-access-key"
export AWS_SECRET_ACCESS_KEY="your-secret-key"
export AWS_DEFAULT_REGION="ap-northeast-1"

# データベース設定
export DATABASE_URL="postgresql://username:password@host:5432/database"
export PGUSER="username"
export PGPASSWORD="password"
export PGDATABASE="database"
export PGHOST="host"
export PGPORT="5432"

# S3バケット設定
export S3_BUCKET_NAME="your-bucket-name"
```

### 3. 依存関係のインストール

```bash
pip install gradio sqlalchemy boto3 psycopg2-binary
```

### 4. インフラストラクチャのセットアップ

```bash
cd infrastructure/terraform
terraform init
terraform apply
```

必要な情報を入力してインフラを構築します。

### 5. データベースのマイグレーション

```bash
psql -h $PGHOST -U $PGUSER -d $PGDATABASE -f infrastructure/migrations/001_create_cats_table.sql
```

### 6. アプリケーションの起動

```bash
python gradio/app.py
```

アプリケーションは http://localhost:5000 で利用可能になります。

## トラブルシューティング

### データベース接続エラー
- 環境変数が正しく設定されているか確認
- PostgreSQLサービスが実行中か確認
- ファイアウォール設定を確認

### S3アップロードエラー
- AWS認証情報が正しく設定されているか確認
- バケットの権限設定を確認
- バケット名が正しいか確認
