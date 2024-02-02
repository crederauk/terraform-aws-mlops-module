# ECR
output "ecr_repository" {
  description = "The ECR repository Terraform object."
  value       = module.ecr.repository
}

output "ecr" {
  description = "The ECR repository module outputs. Contains both 'repository' and 'encryption_key' attributes, that are the ECR repository and KMS encryption key Terraform object respectively."
  value       = module.ecr
}

# Glue
output "glue" {
  description = "The Glue module outputs. Contains both 'retraining_job' and 'retraining_role' attributes, that are the Glue retraining job and IAM role Terraform objects respectively."
  value       = one(module.retraining_job[*])
}

output "glue_retraining_role" {
  description = "The Glue retraining job IAM role Terraform object."
  value       = one(module.retraining_job[*].retraining_role)
}

# S3
output "config_bucket" {
  description = "Config S3 Bucket Terraform object"
  value       = module.s3.config_bucket
}

output "model_bucket" {
  description = "Model S3 Bucket Terraform object"
  value       = module.s3.model_bucket
}

output "s3_encryption_key" {
  description = "S3 encryption KMS key Terraform Object"
  value       = module.s3.encryption_key
}

# Sagemaker
output "sagemaker_notebook_instance" {
  description = "Sagemaker notebook instance Terraform object"
  value       = module.sagemaker.notebook_instance
}

output "sagemaker_endpoint_name" {
  description = "Sagemaker model endpoint name"
  value       = module.sagemaker.endpoint_name
}

output "sagemaker_model_name" {
  description = "Sagemaker model name"
  value       = module.sagemaker.model_name
}

