output "retraining_job" {
  description = "The Glue retraining job Terraform object."
  value       = aws_glue_job.retraining_job
}

output "retraining_role" {
  description = "The Glue retraining job IAM role Terraform object."
  value       = aws_iam_role.glue_retraining_job
}
