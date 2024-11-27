# インフラストラクチャガイド

## AWS構成

### 概要
本システムは以下のAWSサービスを使用します：

1. Amazon RDS (PostgreSQL)
   - データベースエンジン: PostgreSQL 14.6
   - インスタンスクラス: db.t3.micro
   - ストレージ: 20GB (gp2)

2. Amazon S3
   - 画像ストレージ用バケット
   - パブリックアクセス設定あり

### アーキテクチャ図
```
[Gradio App] ─── [Amazon RDS PostgreSQL]
     │
     └──────── [Amazon S3]
```

## Terraformの使用方法

### 1. 初期設定

`infrastructure/terraform`ディレクトリに移動し、以下のコマンドを実行：

```bash
terraform init
```

### 2. 変数の設定

以下の変数を`terraform.tfvars`ファイルで設定：

```hcl
aws_region         = "ap-northeast-1"
vpc_cidr          = "10.0.0.0/16"
database_name     = "cat_registry"
database_username = "admin"
database_password = "your-secure-password"
s3_bucket_name    = "your-bucket-name"
```

### 3. プランの確認

```bash
terraform plan
```

### 4. インフラの作成

```bash
terraform apply
```

### 5. インフラの削除

```bash
terraform destroy
```

## データベース設計

### テーブル構造

#### cats テーブル
```sql
CREATE TABLE cats (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) NOT NULL,
    age INTEGER NOT NULL,
    breed VARCHAR(100) NOT NULL,
    image_url VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_cats_created_at ON cats(created_at DESC);
```

### インデックス
- `idx_cats_created_at`: 作成日時による降順ソート用

## セキュリティ設定

### RDSセキュリティ
- VPC内での実行
- セキュリティグループによるアクセス制御
- SSL/TLS暗号化の使用

### S3セキュリティ
- パブリックアクセス設定
- CORS設定
- バケットポリシーによるアクセス制御

## バックアップと復元

### RDSバックアップ
- 自動バックアップ: 7日間保持
- スナップショット: 手動で作成可能

### S3バックアップ
- バージョニング機能の利用
- クロスリージョンレプリケーション（オプション）

## モニタリング

### CloudWatch設定
- RDSメトリクス監視
- S3アクセスログ
- アラート設定

## スケーリング戦略

### RDSスケーリング
- インスタンスクラスのアップグレード
- ストレージの自動拡張

### S3スケーリング
- 自動的にスケール
- 特別な設定不要
