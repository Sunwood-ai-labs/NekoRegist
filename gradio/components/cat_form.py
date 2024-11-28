import gradio as gr
from utils.db import add_cat
from utils.s3 import upload_image
import uuid

def create_cat_form():
    """猫の情報を入力するフォームを作成"""
    with gr.Group():
        with gr.Row():
            name = gr.Textbox(label="名前", placeholder="例：タマ")
            age = gr.Number(label="年齢", minimum=0, maximum=30, value=1)
            breed = gr.Textbox(label="品種", placeholder="例：雑種")
        
        with gr.Row():
            image = gr.Image(label="写真", type="filepath")
        
        with gr.Row():
            submit_btn = gr.Button("登録", variant="primary")
            output = gr.Markdown()

        def handle_submit(name_val, age_val, breed_val, image_val):
            """
            フォームの送信処理
            """
            try:
                # 入力値のバリデーション
                if not name_val or age_val is None or not breed_val:
                    return "すべての項目を入力してください。"

                # 画像のアップロード
                image_url = None
                if image_val:
                    image_key = f"cats/{str(uuid.uuid4())}.jpg"
                    image_url = upload_image(image_val, image_key)

                # データベースに保存
                cat_id = add_cat(name_val, int(age_val), breed_val, image_url)
                
                # フォームをクリア
                return gr.update(value=""), gr.update(value=1), gr.update(value=""), gr.update(value=None), f"猫の登録が完了しました！ (ID: {cat_id})"
            except Exception as e:
                return [gr.update() for _ in range(4)] + [f"エラーが発生しました: {str(e)}"]

        # イベントハンドラーの設定
        submit_btn.click(
            fn=handle_submit,
            inputs=[name, age, breed, image],
            outputs=[name, age, breed, image, output]
        )

        return name, age, breed, image, output
