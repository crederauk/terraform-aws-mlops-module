output "config_bucket" {
  description = "Config S3 Bucket Terraform object"
  value       = aws_s3_bucket.model_buckets[1]
}

output "model_bucket" {
  description = "Model S3 Bucket Terraform object"
  value       = aws_s3_bucket.model_buckets[0]
}

output "encryption_key" {
  description = "S3 encryption KMS key Terraform Object"
  value       = aws_kms_key.model_buckets
}
