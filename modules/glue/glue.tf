#Upload retraining_job.py to s3
resource "aws_s3_object" "retraining_job_script" {
  bucket = var.config_s3_bucket
  key    = "glue_scripts/retraining_job.py"
  source = "${path.module}/glue_jobs/retraining_job.py"
  etag   = filemd5("${path.module}/glue_jobs/retraining_job.py")
  tags   = var.tags
}

#####Retraining Glue job#####

resource "aws_glue_job" "retraining_job" {
  name     = aws_iam_role.glue_retraining_job.name
  role_arn = aws_iam_role.glue_retraining_job.arn

  command {
    script_location = "s3://${var.config_s3_bucket}/glue_scripts/retraining_job.py"
  }

  default_arguments = {
    "--job-language"        = "python"
    "--glue_version"        = "3.0"
    "--enable-metrics"      = "true"
    "--data_location_s3"    = "${var.data_s3_bucket}${var.data_location_s3}"
    "--job-bookmark-option" = "job-bookmark-enable"
  }
  tags = var.tags
}


#Retraining Glue job trigger
resource "aws_glue_trigger" "retraining_job" {
  name = "${var.resource_naming_prefix}_retraining_glue_job_trigger"

  schedule = var.retraining_schedule
  type     = "SCHEDULED"

  actions {
    job_name = aws_glue_job.retraining_job.name
  }
  tags = var.tags
}
