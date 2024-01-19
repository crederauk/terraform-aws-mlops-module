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

#########################################
# Sagemaker
#########################################

# Training
variable "algorithm_choice" {
  description = "Machine learning problem type e.g classification, regression, clustering, anomaly, time_series"
  type        = string
}
variable "tuning_metric" {
  description = "The metric user want to focus when tuning hyperparameter"
  type        = string
}

# Notebook
variable "training_notebook_instance_type" {
  description = "The Sagemaker notebook instance type to be created for training the model. Must be a valid EC2 instance type"
  type        = string
}

# Model
variable "inference_instance_type" {
  description = "The instance type to be created for serving the model. Must be a valid EC2 instance type"
  default     = "ml.t2.medium"
  type        = string
}
variable "inference_instance_count" {
  description = "The initial number of instances to serve the model endpoint"
  type        = number
}
variable "model_target_variable" {
  description = "The dependent variable (or 'label') that the model aims to predict. This should be a column name in the dataset."
  type        = string
}
variable "ecr_repo_uri" {
  description = "The URI of the ECR repository containing the pycaret image, including tag."
  type        = string
}

#########################################
# S3
#########################################

# Data bucket
variable "data_s3_bucket" {
  description = "The name of an S3 bucket within which training data is located."
  type        = string
}
variable "data_location_s3" {
  description = "The path to a file in the data S3 bucket within which training data is located. Should be in the format /<path>/<filename>. If the data is in the root of the bucket, this should be set to /<filename> only."
  type        = string
}
variable "data_bucket_key_arn" {
  description = "The ARN of the KMS key using which data is encrypted in S3."
  type        = string
}

# Model bucket
variable "model_s3_bucket" {
  description = "The name of an S3 bucket within which the model artifact should be saved."
  type        = string
}
variable "model_bucket_key_arn" {
  description = "The ARN of the KMS key that has been used to encrypted the S3 bucket."
  type        = string
}

# Config Bucket
variable "config_s3_bucket" {
  description = "The name of the S3 bucket within which notebook scripts are stored, to be copied onto the instance on boot."
  type        = string
}
variable "config_bucket_key_arn" {
  description = "The ARN of the KMS key using which notebook scripts are encrypted in S3."
  type        = string
}
