import os
import gradio as gr
import logging
from components.cat_form import create_cat_form
from components.cat_list import create_cat_list
from utils.db import init_db
from utils.s3 import init_s3

# ロギングの設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def initialize_services():
    """サービスの初期化"""
    try:
        # データベース初期化
        logger.info("データベースを初期化中...")
        init_db()
        logger.info("データベース初期化完了")

        # S3初期化
        logger.info("S3接続を初期化中...")
        init_s3()
        logger.info("S3接続初期化完了")

        return True
    except Exception as e:
        logger.error(f"初期化エラー: {str(e)}")
        raise e


def create_app():
    # サービスの初期化
    initialize_services()

    # アプリケーション作成
    with gr.Blocks(title="猫登録システム", theme=gr.themes.Ocean()) as app:
        gr.Markdown("# 🐱 猫登録システム")

        with gr.Tabs():
            with gr.Tab("新規登録"):
                create_cat_form()

            with gr.Tab("登録済み猫一覧"):
                create_cat_list()

    return app


if __name__ == "__main__":
    try:
        app = create_app()
        app.launch(server_name="0.0.0.0", server_port=5000)
    except Exception as e:
        logger.error(f"アプリケーション起動エラー: {str(e)}")
        raise e
