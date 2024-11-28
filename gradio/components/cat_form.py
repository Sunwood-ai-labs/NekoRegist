import gradio as gr
from utils.db import add_cat
from utils.s3 import upload_image
import uuid

def create_cat_form():
    with gr.Group():
        name = gr.Textbox(label="名前")
        age = gr.Number(label="年齢", minimum=0, maximum=30)
        breed = gr.Textbox(label="品種")
        image = gr.Image(label="写真", type="filepath")
        submit_btn = gr.Button("登録", variant="primary")

        output = gr.Markdown()

        def handle_submit(name, age, breed, image):
            try:
                if not name or not age or not breed:
                    return "すべての項目を入力してください。"

                # 画像のアップロード
                image_url = None
                if image:
                    image_key = f"cats/{str(uuid.uuid4())}.jpg"
                    image_url = upload_image(image, image_key)

                # データベースに保存
                cat_id = add_cat(name, int(age), breed, image_url)
                return f"猫の登録が完了しました！ (ID: {cat_id})"

            except Exception as e:
                return f"エラーが発生しました: {str(e)}"

        submit_btn.click(
            fn=handle_submit,
            inputs=[name, age, breed, image],
            outputs=[output]
        )
