# AWS-MLOps-module

## [2.0.0] - 21/12/23
**BREAKING CHANGES**
* Mandatory variable `resource_naming_prefix` has now been added.
* Mandatory variable `data_s3_bucket` has now been added.
* Variable `model_instance_count` has been renamed `inference_instance_count`
* Variable `sagemaker_instance_type` has been replaced with two variables:
  * `sagemaker_training_notebook_instance_type`, which now defines the type of the training notebook only.
  * `inference_instance_type`, which now defines the type of instance used to serve the model only.
* The syntax for `data_location_s3` has now changed - should not include bucket name.
* `region` and `account_id` variables have been removed - no longer required.
* All outputs have now been refactored to be more useful.
* When creating a Docker container from the image in this module, `MODEL_NAME` and `MODEL_TYPE` must now be passed in as environment variables.
* `random` provider is now required to generate suffix for globally unique bucket names
* Permissions have been locked down:
  * Lambdas can no longer assume the created Sagemaker IAM role by default.
  * Glue IAM role and Sagemaker IAM role no longer have access to all KMS keys in the account. They are only given access to required S3 bucket encryption keys.
  * `iam:PassRole` permission has been removed from the Sagemaker IAM Role

**Features**
* Now supports training data stored in an encrypted s3 bucket.

## [1.0.8] - 27/10/23
* Provided a module usage example in README, removed currently unnecesary code, added model and endpoint outputs

## [1.0.7] - 29/09/23
* Removed Lambda resorces, added domain and Glue resources

## [1.0.6] - 18-08-2023
* Lambda zip file fix

## [1.0.5] - 18-08-2023
* Added tfsec job to CICD pipeline

## [1.0.4] - 04-08-2023
* Added the lambda resource

## [1.0.3] - 04-08-2023
* Added CICD pipeline to trigger on commit with the following stages: tf format, tf validate, tflint, pytest, pylint, Flake8, terratest

## [1.0.2] - 14-07-2023
* Added S3, iam, sagemaker resources
  
## [1.0.1] - 09-06-2023
* Added S3 resources

## [1.0.0] - 09-06-2023
* Added basic repo structure and basic resource to test integration with streaming-data-platform
