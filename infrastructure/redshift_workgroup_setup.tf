provider "aws" {
  region = "us-east-1"
}

resource "aws_redshiftserverless_namespace" "logs_namespace" {
  namespace_name = "logs_namespace"
  admin_username = "your_username"
  admin_password = "Your_password"
  db_name        = "your_db_name"
}

resource "aws_redshiftserverless_workgroup" "logs_workgroup" {
  workgroup_name = "Your Redshift WorkGroup Name"
  namespace_name = aws_redshiftserverless_namespace.logs_namespace.namespace_name
  base_capacity  = 8  # RPUs

  # Network/security settings
  subnet_ids         = ["subnet-xxxxxx1", "subnet-xxxxxx2"]  # Replace with your subnets
  security_group_ids = ["sg-xxxxxx"]                         # Replace with your SG
}

# Security group rule for Databricks access
resource "aws_security_group_rule" "redshift_ingress" {
  type              = "ingress"
  from_port         = 5439
  to_port           = 5439
  protocol          = "tcp"
  cidr_blocks       = ["0.0.0.0/0"]  # Restrict to Databricks IP in production
  security_group_id = "sg-xxxxxx"     # Replace with your SG ID
}