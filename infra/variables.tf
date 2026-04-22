variable "aws_region" {
  type        = string
  default     = "us-east-1"
  description = "AWS region for all resources."
}

variable "project_name" {
  type        = string
  default     = "dc-ops-dashboard"
  description = "Prefix used for AWS resources."
}

variable "container_port" {
  type        = number
  default     = 8501
  description = "Streamlit container port."
}

variable "container_image" {
  type        = string
  description = "ECR image URI including tag, for example 123456789012.dkr.ecr.us-east-1.amazonaws.com/dc-ops-dashboard:latest."
}

variable "public_subnet_ids" {
  type        = list(string)
  description = "Public subnet IDs where ALB and ECS tasks run."
}

variable "vpc_id" {
  type        = string
  description = "VPC ID for ECS and ALB resources."
}
