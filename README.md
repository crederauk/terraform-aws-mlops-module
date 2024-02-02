# AWS-MLOps-module
This repo contains a terraform module with corresponding AWS resources that enable training, deploying and re-training AWS-hosted machine learning models with corresponding cloud infrastructure.

>  **Warning**: This repo is a basic template for MLOps resources on AWS. Please apply appropriate security enhancements for your project in production.

## High-Level Solution Architecture
![image](https://github.com/konradbachusz/AWS-MLOps-module/assets/104912687/12c4f1a0-573b-44a0-98f2-1256be64d19a)


## Example Usage

 ```
module "MLOps" {
  source  = "github.com/crederauk/terraform-aws-mlops-module?ref=<MODULE_VERSION>"
  resource_naming_prefix  = "your-app"
  data_s3_bucket          = "your-bucket-name"
  data_location_s3        = "/your_s3_folder/your_data.csv"
  data_s3_bucket_encryption_key_arn = "arn:aws:your_kms_key_arn"
  model_target_variable   = "y"
  model_name              = "your-ml-model"
  retrain_model_bool      = true
  retraining_schedule     = "cron(0 8 1 * ? *)"
  algorithm_choice        = "classification"
  sagemaker_training_notebook_instance_type = "ml.m4.xlarge"
  inference_instance_type     = "ml.m4.xlarge"
  inference_instance_count    = 1
  tuning_metric = "AUC"
  tags                    = {
                              my-tag-key = "my-tag-value"
                            }
} 
```

<!-- BEGIN_TF_DOCS -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | >= 1.0 |
| <a name="requirement_archive"></a> [archive](#requirement\_archive) | 2.4.0 |
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | >= 4.0 |
| <a name="requirement_local"></a> [local](#requirement\_local) | >= 2.4 |
| <a name="requirement_random"></a> [random](#requirement\_random) | >= 3.6 |

## Providers

No providers.

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_ecr"></a> [ecr](#module\_ecr) | ./modules/ecr | n/a |
| <a name="module_retraining_job"></a> [retraining\_job](#module\_retraining\_job) | ./modules/glue | n/a |
| <a name="module_s3"></a> [s3](#module\_s3) | ./modules/s3 | n/a |
| <a name="module_sagemaker"></a> [sagemaker](#module\_sagemaker) | ./modules/sagemaker | n/a |

## Resources

No resources.

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_algorithm_choice"></a> [algorithm\_choice](#input\_algorithm\_choice) | Machine learning problem type e.g classification, regression, clustering, anomaly, time\_series | `string` | n/a | yes |
| <a name="input_data_location_s3"></a> [data\_location\_s3](#input\_data\_location\_s3) | The path to a file in the data S3 bucket within which training data is located. Should be in the format /<path>/<filename>. If the file is in the root of the bucket, this should be set to /<filename> only. | `string` | n/a | yes |
| <a name="input_data_s3_bucket"></a> [data\_s3\_bucket](#input\_data\_s3\_bucket) | The name of an S3 bucket within which training data is located. | `string` | n/a | yes |
| <a name="input_data_s3_bucket_encryption_key_arn"></a> [data\_s3\_bucket\_encryption\_key\_arn](#input\_data\_s3\_bucket\_encryption\_key\_arn) | The ARN of the KMS key using which training data is encrypted in S3, if such a key exists. | `string` | `""` | no |
| <a name="input_inference_instance_count"></a> [inference\_instance\_count](#input\_inference\_instance\_count) | The initial number of instances to serve the model endpoint | `number` | `1` | no |
| <a name="input_inference_instance_type"></a> [inference\_instance\_type](#input\_inference\_instance\_type) | The instance type to be created for serving the model. Must be a valid EC2 instance type | `string` | `"ml.t2.medium"` | no |
| <a name="input_model_target_variable"></a> [model\_target\_variable](#input\_model\_target\_variable) | The dependent variable (or 'label') that the model aims to predict. This should be a column name in the dataset. | `string` | n/a | yes |
| <a name="input_resource_naming_prefix"></a> [resource\_naming\_prefix](#input\_resource\_naming\_prefix) | Naming prefix to be applied to all resources created by this module | `string` | n/a | yes |
| <a name="input_retrain_model_bool"></a> [retrain\_model\_bool](#input\_retrain\_model\_bool) | Boolean to indicate if the retraining pipeline shoud be added | `bool` | `false` | no |
| <a name="input_retraining_schedule"></a> [retraining\_schedule](#input\_retraining\_schedule) | Cron expression for the model retraining frequency in the AWS format. See https://docs.aws.amazon.com/lambda/latest/dg/services-cloudwatchevents-expressions.html for details | `string` | `""` | no |
| <a name="input_sagemaker_training_notebook_instance_type"></a> [sagemaker\_training\_notebook\_instance\_type](#input\_sagemaker\_training\_notebook\_instance\_type) | The Sagemaker notebook instance type to be created for training the model. Must be a valid EC2 instance type | `string` | `"ml.t2.medium"` | no |
| <a name="input_tags"></a> [tags](#input\_tags) | Tags applied to your resources | `map(string)` | `{}` | no |
| <a name="input_tuning_metric"></a> [tuning\_metric](#input\_tuning\_metric) | The metric user want to focus when tuning hyperparameter | `string` | n/a | yes |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_config_bucket"></a> [config\_bucket](#output\_config\_bucket) | Config S3 Bucket Terraform object |
| <a name="output_ecr"></a> [ecr](#output\_ecr) | The ECR repository module outputs. Contains both 'repository' and 'encryption\_key' attributes, that are the ECR repository and KMS encryption key Terraform object respectively. |
| <a name="output_ecr_repository"></a> [ecr\_repository](#output\_ecr\_repository) | The ECR repository Terraform object. |
| <a name="output_glue"></a> [glue](#output\_glue) | The Glue module outputs. Contains both 'retraining\_job' and 'retraining\_role' attributes, that are the Glue retraining job and IAM role Terraform objects respectively. |
| <a name="output_glue_retraining_role"></a> [glue\_retraining\_role](#output\_glue\_retraining\_role) | The Glue retraining job IAM role Terraform object. |
| <a name="output_model_bucket"></a> [model\_bucket](#output\_model\_bucket) | Model S3 Bucket Terraform object |
| <a name="output_s3_encryption_key"></a> [s3\_encryption\_key](#output\_s3\_encryption\_key) | S3 encryption KMS key Terraform Object |
| <a name="output_sagemaker_endpoint_name"></a> [sagemaker\_endpoint\_name](#output\_sagemaker\_endpoint\_name) | Sagemaker model endpoint name |
| <a name="output_sagemaker_model_name"></a> [sagemaker\_model\_name](#output\_sagemaker\_model\_name) | Sagemaker model name |
| <a name="output_sagemaker_notebook_instance"></a> [sagemaker\_notebook\_instance](#output\_sagemaker\_notebook\_instance) | Sagemaker notebook instance Terraform object |

## Destroying Resources
After creating the resources made using this the module, the resources: 
- Sagemaker model 
- Sagemaker Endpoint  
- Endpoint configuration
  
Will not be tracked by your Terraform state file so if you decide to run "terraform destroy" these resources will not be deleted.

To destroy these resourses we recommend that you add these commands to your CI/CD pipeline:

```bash
aws sagemaker delete-model --model-name < demo-regression-model >
aws sagemaker delete-endpoint-config --endpoint-config-name < demo-regression-model-config >
aws sagemaker delete-endpoint --endpoint-name < demo-regression-model >    
```

But before this you will need to add your AWS credentials to the environment if you have not do already:
```bash
aws-access-key-id: < aws-access-key-id >
aws-secret-access-key: < aws-secret-access-key >
aws-region: < region >
```
<!-- END_TF_DOCS -->
