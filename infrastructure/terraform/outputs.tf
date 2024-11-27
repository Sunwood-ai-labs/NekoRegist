output "rds_endpoint" {
  description = "RDS instance endpoint"
  value       = aws_db_instance.postgres.endpoint
}

output "s3_bucket_name" {
  description = "Name of the S3 bucket for cat images"
  value       = aws_s3_bucket.cat_images.id
}
