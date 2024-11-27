# 開発ガイド

## 開発環境のセットアップ

### 1. 開発用の依存関係
開発環境では、本番環境の依存関係に加えて以下のパッケージを使用します：

```bash
pip install pytest pytest-cov black flake8
```

### 2. コーディング規約

#### Python コードスタイル
- PEP 8に準拠
- Black形式を使用
- 行の最大長は88文字
- インデントは4スペース

#### 命名規則
- クラス名: UpperCamelCase
- 関数名: snake_case
- 変数名: snake_case
- 定数: UPPER_SNAKE_CASE

### 3. プロジェクト構造
```
gradio/
├── components/      # UIコンポーネント
├── utils/          # ユーティリティ関数
└── app.py          # メインアプリケーション

infrastructure/
├── migrations/     # データベースマイグレーション
└── terraform/      # インフラ構成
```

### 4. コンポーネント開発

#### 新しいコンポーネントの追加
1. `gradio/components/`に新しいPythonファイルを作成
2. コンポーネントのクラスまたは関数を実装
3. `app.py`でコンポーネントをインポートして使用

例：
```python
import gradio as gr

def create_new_component():
    with gr.Group():
        # コンポーネントの実装
        pass
```

### 5. テスト

#### テストの実行
```bash
pytest tests/
```

#### カバレッジレポートの生成
```bash
pytest --cov=gradio tests/
```

### 6. コードの品質チェック

#### Blackでのフォーマット
```bash
black gradio/
```

#### Flake8での静的解析
```bash
flake8 gradio/
```

## CI/CDパイプライン

GitHub Actionsを使用して以下を自動化：
1. コードの品質チェック
2. テストの実行
3. カバレッジレポートの生成
4. 本番環境へのデプロイ

## デバッグ

### ログの確認
- アプリケーションログは標準出力に出力
- データベースのログは PostgreSQL のログファイルを確認

### デバッグモード
開発時は`debug=True`を設定：

```python
app.launch(server_name="0.0.0.0", server_port=5000, debug=True)
```
