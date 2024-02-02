##########################################
# Naming and Tagging
##########################################

variable "resource_naming_prefix" {
  description = "Naming prefix to be applied to all resources created by this module"
  type        = string
}
variable "tags" {
  description = "Tags applied to your resources"
  default     = {}
  type        = map(string)
}

##########################################
# Sagemaker
##########################################

variable "sagemaker_training_notebook_instance_type" {
  description = "The Sagemaker notebook instance type to be created for training the model. Must be a valid EC2 instance type"
  default     = "ml.t2.medium"
  type        = string
}
variable "inference_instance_type" {
  description = "The instance type to be created for serving the model. Must be a valid EC2 instance type"
  default     = "ml.t2.medium"
  type        = string
}
variable "inference_instance_count" {
  description = "The initial number of instances to serve the model endpoint"
  type        = number
  default     = 1
}

##########################################
# S3
##########################################

variable "data_s3_bucket" {
  description = "The name of an S3 bucket within which training data is located."
  type        = string
}
variable "data_s3_bucket_encryption_key_arn" {
  description = "The ARN of the KMS key using which training data is encrypted in S3, if such a key exists."
  type        = string
  default     = ""
  validation {
    condition     = (substr(var.data_s3_bucket_encryption_key_arn, 0, 8) == "arn:aws:") || (var.data_s3_bucket_encryption_key_arn == "")
    error_message = "The data_s3_bucket_encryption_key_arn value must be a valid ARN, starting with \"arn:aws:\"."
  }
}
variable "data_location_s3" {
  description = "The path to a file in the data S3 bucket within which training data is located. Should be in the format /<path>/<filename>. If the file is in the root of the bucket, this should be set to /<filename> only."
  type        = string
  validation {
    condition     = substr(var.data_location_s3, 0, 1) == "/"
    error_message = "The data_location_s3 value must begin with /."
  }
}

##########################################
# Glue
##########################################

variable "retraining_schedule" {
  description = "Cron expression for the model retraining frequency in the AWS format. See https://docs.aws.amazon.com/lambda/latest/dg/services-cloudwatchevents-expressions.html for details"
  type        = string
  default     = ""
  validation {
    condition     = contains(["cron(", "rate("], substr(var.retraining_schedule, 0, 4)) || (var.retraining_schedule == "")
    error_message = "The retraining_schedule value must begin with \"cron(\" or \"rate(\"."
  }
}
variable "retrain_model_bool" {
  description = "Boolean to indicate if the retraining pipeline shoud be added"
  type        = bool
  default     = false
}

##########################################
# Model arguments
##########################################

variable "model_target_variable" {
  description = "The dependent variable (or 'label') that the model aims to predict. This should be a column name in the dataset."
  type        = string
}
variable "algorithm_choice" {
  description = "Machine learning problem type e.g classification, regression, clustering, anomaly, time_series"
  type        = string
  validation {
    condition     = contains(["classification", "regression", "clustering", "anomaly", "time_series"], var.algorithm_choice)
    error_message = "Allowed values for algorithm_choice are \"classification\", \"regression\", \"clustering\",  \"anomaly\", or \"time_series\"."
  }
}
variable "tuning_metric" {
  description = "The metric user want to focus when tuning hyperparameter"
  type        = string
}
