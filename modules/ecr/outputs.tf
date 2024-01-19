output "repository" {
  description = "The ECR repository Terraform object."
  value       = aws_ecr_repository.pycaret
}

output "encryption_key" {
  description = "The ECR repository encryption KMS key Terraform object."
  value       = aws_kms_key.ecr_encryption
}
