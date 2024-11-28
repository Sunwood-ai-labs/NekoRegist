<div align="center">

![](../assets/header_infra.svg)

</div>

# インフラストラクチャ

## 概要
本システムはAWSのマネージドサービスを活用し、スケーラブルで信頼性の高いインフラストラクチャを実現しています。

## AWS構成

### 使用サービス
1. **Amazon RDS (PostgreSQL)**
   - エンジン: PostgreSQL 16.3
   - インスタンス: db.t3.micro
   - ストレージ: 20GB (gp2)
   - 自動バックアップ: 7日間保持

2. **Amazon S3**
   - 用途: 画像ストレージ
   - バケット設定: パブリックアクセス制限
   - バージョニング: 有効

### アーキテクチャ構成
```
[Gradio App] ─── [Amazon RDS PostgreSQL]
     │
     └──────── [Amazon S3]
```

## Terraform構成

### ファイル構造
```
terraform/
├── provider.tf    - AWSプロバイダーの設定
├── vpc.tf         - VPCとネットワーク関連リソース
├── rds.tf         - RDS関連リソース
├── s3.tf          - S3バケット関連リソース
├── variables.tf    - 変数定義
├── outputs.tf      - 出力定義
└── terraform.tfvars - 変数値の設定
```

### 主要コンポーネント
1. **VPC設定**
   - パブリック/プライベートサブネット
   - NAT Gateway
   - Internet Gateway
   - 適切なルーティング設定

2. **RDS設定**
   - セキュリティグループ
   - サブネットグループ
   - PostgreSQLインスタンス

3. **S3設定**
   - バケット作成
   - パブリックアクセス設定

## データベース設計

### テーブル構造
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

### インデックス最適化
- `idx_cats_created_at`: 一覧表示の高速化
- 必要に応じて追加のインデックスを検討

## デプロイメントガイド

### 前提条件
1. AWSアカウントとアクセス権限
2. Terraformのインストール (1.0以上)
3. 環境変数の設定
   ```bash
   # AWS認証情報
   AWS_ACCESS_KEY_ID
   AWS_SECRET_ACCESS_KEY
   AWS_DEFAULT_REGION
   ```

### デプロイ手順
1. Terraformによるインフラ構築
   ```bash
   cd terraform
   terraform init
   terraform plan
   terraform apply
   ```

2. 環境変数の設定（terraform outputから取得）
   ```bash
   # データベース接続情報
   export DATABASE_URL="postgres://${username}:${password}@${rds_endpoint}/${database_name}"
   export PGUSER=${username}
   export PGPASSWORD=${password}
   export PGDATABASE=${database_name}
   export PGHOST=${rds_host}
   export PGPORT=5432

   # S3設定
   export S3_BUCKET_NAME=${bucket_name}
   ```

3. データベースマイグレーション
4. アプリケーションのデプロイ

### 監視設定
1. CloudWatchメトリクス
2. アラート設定
3. ログ管理

## セキュリティ設定

### データベースセキュリティ
1. **ネットワーク**
   - VPC内での実行
   - セキュリティグループによるアクセス制限
   - SSL/TLS暗号化

2. **認証・認可**
   - IAMデータベース認証
   - 最小権限の原則

### S3セキュリティ
1. **アクセス制御**
   - バケットポリシー
   - CORS設定
   - 暗号化設定

2. **データ保護**
   - バージョニング
   - アクセスログ
   - 署名付きURL

### 運用セキュリティ
1. **監査**
   - CloudTrail有効化
   - アクセスログ分析
   - 定期的なセキュリティレビュー

2. **コンプライアンス**
   - 暗号化標準の遵守
   - アクセス管理の文書化
   - 定期的な脆弱性診断