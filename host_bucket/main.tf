# TODO: Configure to be private
resource "aws_s3_bucket" "module-registry" {
  bucket = var.bucket_name
}

# TODO: Add IAM role that has permissions to upload to bucket only, to be assumed in pipeline.
