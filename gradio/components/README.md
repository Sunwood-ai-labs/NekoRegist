# Gradioコンポーネント

## 概要
このディレクトリには、アプリケーションのUIを構成するGradioコンポーネントが含まれています。各コンポーネントは特定の機能に特化し、再利用可能な形で実装されています。

## コンポーネント一覧

### cat_form.py
猫の情報を登録するためのフォームコンポーネント

#### 機能
- 名前、年齢、品種、写真の入力フィールド
- 入力値のバリデーション
- S3への画像アップロード
- データベースへの保存

#### 使用方法
```python
from components.cat_form import create_cat_form

with gr.Blocks() as app:
    create_cat_form()
```

### cat_list.py
登録済みの猫一覧を表示するコンポーネント

#### 機能
- 登録済み猫の一覧表示
- 画像のプレビュー
- 情報の更新機能

#### 使用方法
```python
from components.cat_list import create_cat_list

with gr.Blocks() as app:
    create_cat_list()
```

## 開発ガイドライン
1. 新しいコンポーネントを追加する場合は、このディレクトリに配置
2. コンポーネントごとに独立した.pyファイルを作成
3. 共通のユーティリティ関数は`utils`ディレクトリに配置
4. コンポーネントの関数名は`create_*`の形式に統一
