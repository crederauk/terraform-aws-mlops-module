output "notebook_instance" {
  description = "Sagemaker notebook instance Terraform object"
  value       = aws_sagemaker_notebook_instance.training_notebook
}

output "role" {
  description = "Sagemaker IAM role Terraform object"
  value       = aws_iam_role.sagemaker
}

output "endpoint_name" {
  description = "Sagemaker model endpoint name"
  value       = local.endpoint_name
}

output "model_name" {
  description = "Sagemaker model name"
  value       = local.model_name
}
