terraform {
  backend "s3" {}
}

provider "aws" {
  default_tags {
    tags = {
      Environment = "sandpit"
      CreatedBy   = "Terraform"
      Repository  = "AWS-MLOps-module"
    }
  }
  assume_role {
    role_arn = "arn:aws:iam::135544376709:role/NonprodProvisionerRole"
  }
}
