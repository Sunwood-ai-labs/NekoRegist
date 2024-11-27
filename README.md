# 🐱 猫登録システム

GradioベースのAWS対応猫登録システム（日本語UI）です。

## 機能
- 猫の基本情報登録（名前、年齢、品種、写真）
- 登録済み猫の一覧表示
- AWS S3を使用した画像保存
- AWS RDS PostgreSQLでのデータ管理

## システム要件
- Python 3.8+
- AWS アカウント
- Terraform

## クイックスタート
1. リポジトリのクローン
2. 環境変数の設定
3. Terraformでインフラ構築
4. アプリケーションの起動

詳細な手順は[セットアップガイド](docs/setup.md)を参照してください。

## ドキュメント
- [セットアップガイド](docs/setup.md)
- [開発ガイド](docs/development.md)
- [インフラストラクチャ](docs/infrastructure.md)
