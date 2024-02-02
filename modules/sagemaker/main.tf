resource "aws_sagemaker_notebook_instance" "training_notebook" {
  name                  = aws_sagemaker_notebook_instance_lifecycle_configuration.training_notebook.name
  instance_type         = var.training_notebook_instance_type
  role_arn              = aws_iam_role.sagemaker.arn
  lifecycle_config_name = aws_sagemaker_notebook_instance_lifecycle_configuration.training_notebook.name
  tags                  = var.tags
}


resource "aws_sagemaker_notebook_instance_lifecycle_configuration" "training_notebook" {
  name = "${local.model_name}-notebook-instance"
  on_start = base64encode(templatefile("${path.module}/templates/startupscript.sh.tftpl",
    {
      config_s3_bucket = var.config_s3_bucket
      env = {
        data_location_s3         = "${var.data_s3_bucket}${var.data_location_s3}"
        target                   = var.model_target_variable
        algorithm_choice         = var.algorithm_choice
        endpoint_name            = local.endpoint_name
        model_name               = local.model_name
        model_s3_bucket          = var.model_s3_bucket
        inference_instance_type  = var.inference_instance_type
        inference_instance_count = var.inference_instance_count
        ecr_repo_uri             = var.ecr_repo_uri
        tuning_metric            = var.tuning_metric
      }
    }
  ))
}
