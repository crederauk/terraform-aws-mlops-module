##########################################
# Naming and Tagging
##########################################

variable "resource_naming_prefix" {
  description = "Naming prefix to be attached to every resource created by this module."
  type        = string
}
variable "tags" {
  description = "Tags applied to your resources"
  default     = {}
  type        = map(string)
}

##########################################
# Glue
##########################################

variable "retraining_schedule" {
  description = "Cron expression for the model retraining frequency in the AWS format. See https://docs.aws.amazon.com/lambda/latest/dg/services-cloudwatchevents-expressions.html for details"
  type        = string
}

##########################################
# S3
##########################################

# Data bucket
variable "data_s3_bucket" {
  description = "The name of an S3 bucket within which training data is located."
  type        = string
}
variable "data_bucket_key_arn" {
  description = "The ARN of the KMS key using which data is encrypted in S3."
  type        = string
}
variable "data_location_s3" {
  description = "The path to a file in the data S3 bucket within which training data is located. Should be in the format /<path>/<filename>. If the data is in the root of the bucket, this should be set to /<filename> only."
  type        = string
}

# Config Bucket
variable "config_s3_bucket" {
  description = "The name of the S3 bucket within which notebook scripts are stored, to be copied onto the instance on boot."
  type        = string
}
variable "config_bucket_key_arn" {
  description = "The ARN of the KMS key using which relevant scripts stored in encrypted S3."
  type        = string
}
