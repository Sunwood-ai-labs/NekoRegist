<div align="center">

![](assets/header.svg)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Gradio](https://img.shields.io/badge/Gradio-最新版-orange?logo=gradio)](https://gradio.app/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14-blue?logo=postgresql)](https://www.postgresql.org/)
[![AWS](https://img.shields.io/badge/AWS-対応-orange?logo=amazon-aws)](https://aws.amazon.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Maintained](https://img.shields.io/badge/メンテナンス-実施中-green.svg)](https://github.com/username/repo/graphs/commit-activity)

### 📋 概要

GradioベースのAWS対応猫登録システム（日本語UI）です。シンプルで使いやすい猫の情報管理を実現します。

</div>

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
