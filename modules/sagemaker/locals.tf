locals {
  model_name    = "${var.resource_naming_prefix}-model"
  endpoint_name = "${local.model_name}-endpoint"
}

data "aws_region" "current" {}

data "aws_caller_identity" "current" {}
