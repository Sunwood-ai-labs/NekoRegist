# RDS用のセキュリティグループ
resource "aws_security_group" "rds" {
  name        = "cat-registry-rds-sg"
  description = "Security group for RDS instance"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = [var.vpc_cidr]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "cat-registry-rds-sg"
  }
}

# RDS用のサブネットグループ
resource "aws_db_subnet_group" "rds" {
  name       = "cat-registry-rds"
  subnet_ids = aws_subnet.private[*].id

  tags = {
    Name = "cat-registry-rds-subnet-group"
  }
}

# RDSインスタンス
resource "aws_db_instance" "postgres" {
  identifier           = "cat-registry-db"
  engine              = "postgres"
  engine_version      = "16.3"
  instance_class      = "db.t3.micro"
  allocated_storage   = 20
  storage_type        = "gp2"
  
  db_name             = var.database_name
  username            = var.database_username
  password            = var.database_password
  
  vpc_security_group_ids = [aws_security_group.rds.id]
  db_subnet_group_name   = aws_db_subnet_group.rds.name
  
  skip_final_snapshot = true

  tags = {
    Name = "cat-registry-rds"
  }
}