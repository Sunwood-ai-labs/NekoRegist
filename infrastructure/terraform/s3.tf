# S3バケット
resource "aws_s3_bucket" "cat_images" {
  bucket = replace(var.s3_bucket_name, "_", "-")

  tags = {
    Name = "cat-registry-bucket"
  }
}

resource "aws_s3_bucket_public_access_block" "cat_images" {
  bucket = aws_s3_bucket.cat_images.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}