import boto3
import os

def upload_image(image_path: str, key: str) -> str:
    """
    画像をS3にアップロードし、URLを返す
    """
    try:
        s3 = boto3.client('s3')
        bucket_name = os.environ.get('S3_BUCKET_NAME')
        
        # 画像をアップロード
        s3.upload_file(image_path, bucket_name, key)
        
        # 公開URLを生成
        url = f"https://{bucket_name}.s3.amazonaws.com/{key}"
        return url
    except Exception as e:
        raise Exception(f"画像のアップロードに失敗しました: {str(e)}")
