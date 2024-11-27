import gradio as gr
from utils.db import get_all_cats

def create_cat_list():
    def format_cats():
        cats = get_all_cats()
        if not cats:
            return "登録された猫はいません。"
        
        formatted = "## 登録済みの猫一覧\n\n"
        for cat in cats:
            formatted += f"### {cat.name}\n"
            formatted += f"- 年齢: {cat.age}歳\n"
            formatted += f"- 品種: {cat.breed}\n"
            if cat.image_url:
                formatted += f"![猫の写真]({cat.image_url})\n"
            formatted += "---\n"
        return formatted

    cat_list = gr.Markdown()
    refresh_btn = gr.Button("更新")
    
    refresh_btn.click(
        fn=format_cats,
        inputs=[],
        outputs=[cat_list]
    )
    
    # 初期表示
    cat_list.value = format_cats()
