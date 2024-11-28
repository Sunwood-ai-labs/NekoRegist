import boto3
import os
import logging
from botocore.exceptions import ClientError

def init_s3():
    """
    S3クライアントの初期化と接続テスト
    """
    try:
        s3 = boto3.client('s3')
        # バケットの存在確認
        bucket_name = os.environ.get('S3_BUCKET_NAME')
        s3.head_bucket(Bucket=bucket_name)
        return True
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == '404':
            raise Exception(f"バケット '{bucket_name}' が存在しません")
        elif error_code == '403':
            raise Exception("S3バケットへのアクセス権限がありません")
        else:
            raise Exception(f"S3接続エラー: {str(e)}")
    except Exception as e:
        raise Exception(f"S3初期化エラー: {str(e)}")

def upload_image(image_path: str, key: str) -> str:
    """
    画像をS3にアップロードし、URLを返す

    Args:
        image_path (str): アップロードする画像のパス
        key (str): S3内でのキー（ファイルパス）

    Returns:
        str: アップロードされた画像のURL

    Raises:
        Exception: アップロード時のエラー
    """
    try:
        s3 = boto3.client('s3')
        bucket_name = os.environ.get('S3_BUCKET_NAME')
        
        # ContentTypeの設定
        content_type = 'image/jpeg' if key.lower().endswith('.jpg') or key.lower().endswith('.jpeg') else 'image/png'
        
        # 画像をアップロード（ContentTypeのみ設定）
        s3.upload_file(
            image_path,
            bucket_name,
            key,
            ExtraArgs={
                'ContentType': content_type
            }
        )
        
        # 署名付きURLを生成（1時間有効）
        url = s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': key},
            ExpiresIn=3600
        )
        return url
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == 'NoSuchBucket':
            raise Exception(f"バケット '{bucket_name}' が存在しません")
        elif error_code == 'AccessDenied':
            raise Exception("S3バケットへのアクセス権限がありません")
        else:
            raise Exception(f"S3アップロードエラー: {str(e)}")
    except Exception as e:
        raise Exception(f"画像のアップロードに失敗しました: {str(e)}")
