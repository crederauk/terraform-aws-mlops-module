module "s3" {
  source = "./modules/s3"

  resource_naming_prefix = var.resource_naming_prefix
  tags                   = var.tags
}

module "sagemaker" {
  source = "./modules/sagemaker"

  # Naming
  resource_naming_prefix = var.resource_naming_prefix
  tags                   = var.tags

  # Training
  algorithm_choice = var.algorithm_choice
  tuning_metric    = var.tuning_metric

  # Notebook
  training_notebook_instance_type = var.sagemaker_training_notebook_instance_type

  # Model
  inference_instance_type  = var.inference_instance_type
  model_target_variable    = var.model_target_variable
  inference_instance_count = var.inference_instance_count
  ecr_repo_uri             = "${module.ecr.repository.repository_url}:latest"

  # S3
  config_s3_bucket      = module.s3.config_bucket.id
  config_bucket_key_arn = module.s3.encryption_key.arn
  data_s3_bucket        = var.data_s3_bucket
  data_bucket_key_arn   = var.data_s3_bucket_encryption_key_arn
  data_location_s3      = var.data_location_s3
  model_s3_bucket       = module.s3.model_bucket.id
  model_bucket_key_arn  = module.s3.encryption_key.arn
}

module "retraining_job" {
  count  = var.retrain_model_bool ? 1 : 0
  source = "./modules/glue"

  # Naming
  resource_naming_prefix = var.resource_naming_prefix
  tags                   = var.tags

  # S3
  config_s3_bucket      = module.s3.config_bucket.id
  config_bucket_key_arn = module.s3.encryption_key.arn
  data_s3_bucket        = var.data_s3_bucket
  data_bucket_key_arn   = var.data_s3_bucket_encryption_key_arn
  data_location_s3      = var.data_location_s3

  # Glue
  retraining_schedule = var.retraining_schedule
}


module "ecr" {
  source = "./modules/ecr"

  resource_naming_prefix = var.resource_naming_prefix
  tags                   = var.tags
}
