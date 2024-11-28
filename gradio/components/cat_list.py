import gradio as gr
from utils.db import get_all_cats

def create_cat_list():
    """登録済みの猫一覧を表示するコンポーネントを作成"""
    def format_cats():
        """
        猫の一覧をMarkdown形式でフォーマット
        """
        try:
            cats = get_all_cats()
            if not cats:
                return "登録された猫はいません。"
            
            formatted = "## 🐱 登録済みの猫一覧\n\n"
            for cat in cats:
                formatted += f"### 🏷️ {cat.name}\n"
                formatted += f"- 🎂 年齢: {cat.age}歳\n"
                formatted += f"- 🐈 品種: {cat.breed}\n"
                if cat.image_url:
                    formatted += f"\n![{cat.name}の写真]({cat.image_url})\n"
                formatted += "\n---\n"
            return formatted
        except Exception as e:
            return f"一覧の取得中にエラーが発生しました: {str(e)}"

    with gr.Group():
        with gr.Row():
            refresh_btn = gr.Button("🔄 更新", variant="secondary")
            cat_list = gr.Markdown()
        
        # イベントハンドラーの設定
        refresh_btn.click(
            fn=format_cats,
            outputs=cat_list
        )
        
        # 初期データの表示
        cat_list.value = format_cats()
        
        return cat_list, refresh_btn
