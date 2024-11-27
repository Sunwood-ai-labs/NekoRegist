import os
import gradio as gr
from components.cat_form import create_cat_form
from components.cat_list import create_cat_list
from utils.db import init_db

def create_app():
    # データベース初期化
    init_db()

    # アプリケーション作成
    with gr.Blocks(title="猫登録システム") as app:
        gr.Markdown("# 🐱 猫登録システム")
        
        with gr.Tabs():
            with gr.Tab("新規登録"):
                create_cat_form()
            
            with gr.Tab("登録済み猫一覧"):
                create_cat_list()

    return app

if __name__ == "__main__":
    app = create_app()
    app.launch(server_name="0.0.0.0", server_port=5000)
