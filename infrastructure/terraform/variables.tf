variable "aws_region" {
  description = "AWS region"
  default     = "ap-northeast-1"
}

variable "vpc_cidr" {
  description = "VPC CIDR block"
  default     = "10.0.0.0/16"
}

variable "database_name" {
  description = "RDS database name"
  type        = string
}

variable "database_username" {
  description = "RDS master username"
  type        = string
}

variable "database_password" {
  description = "RDS master password"
  type        = string
  sensitive   = true
}

variable "s3_bucket_name" {
  description = "S3 bucket name for cat images"
  type        = string
}
