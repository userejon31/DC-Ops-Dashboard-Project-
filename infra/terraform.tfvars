aws_region       = "us-east-1"
project_name     = "dc-ops-dashboard"
container_port   = 8501
container_image  = "REPLACE_WITH_ECR_IMAGE_URI"
vpc_id           = "vpc-xxxxxxxx"
public_subnet_ids = [
  "subnet-xxxxxxxx",
  "subnet-yyyyyyyy"
]
