provider "aws" {
  region = var.aws_region
}

# VPC
resource "aws_vpc" "main" {
  cidr_block = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support = true

  tags = {
    Name = "cat-registry-vpc"
  }
}

# RDS用のサブネットグループ
resource "aws_db_subnet_group" "rds" {
  name       = "cat-registry-rds"
  subnet_ids = aws_subnet.private[*].id
}

# RDSインスタンス
resource "aws_db_instance" "postgres" {
  identifier           = "cat-registry-db"
  engine              = "postgres"
  engine_version      = "14.6"
  instance_class      = "db.t3.micro"
  allocated_storage   = 20
  storage_type        = "gp2"
  
  db_name             = var.database_name
  username            = var.database_username
  password            = var.database_password
  
  vpc_security_group_ids = [aws_security_group.rds.id]
  db_subnet_group_name   = aws_db_subnet_group.rds.name
  
  skip_final_snapshot = true
}

# S3バケット
resource "aws_s3_bucket" "cat_images" {
  bucket = var.s3_bucket_name
}

resource "aws_s3_bucket_public_access_block" "cat_images" {
  bucket = aws_s3_bucket.cat_images.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}
