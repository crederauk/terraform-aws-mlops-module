resource "aws_sagemaker_notebook_instance" "training_notebook" {
  name                  = aws_sagemaker_notebook_instance_lifecycle_configuration.training_notebook.name
  instance_type         = var.training_notebook_instance_type
  role_arn              = aws_iam_role.sagemaker.arn
  lifecycle_config_name = aws_sagemaker_notebook_instance_lifecycle_configuration.training_notebook.name
  tags                  = var.tags
}


resource "aws_sagemaker_notebook_instance_lifecycle_configuration" "training_notebook" {
  name = "${local.model_name}-notebook-instance"
  on_start = base64encode(<<EOL
       #!/bin/bash
       # Location of the scripts
       aws s3 sync s3://${var.config_s3_bucket}/ /home/ec2-user/SageMaker/ --delete --exact-timestamps --exclude "*" --include "*.py" --include "*.ipynb"

       # Make the ipython notebooks editable after copy
       chmod -R 777 /home/ec2-user/SageMaker/

       # Location of the csv file 
       echo "data_location_s3=${var.data_s3_bucket}${var.data_location_s3}" > /home/ec2-user/SageMaker/.env
       echo "target=${var.model_target_variable}" >> /home/ec2-user/SageMaker/.env
       echo "algorithm_choice=${var.algorithm_choice}" >> /home/ec2-user/SageMaker/.env
       echo "endpoint_name=${local.endpoint_name}" >> /home/ec2-user/SageMaker/.env
       echo "model_name=${local.model_name}" >> /home/ec2-user/SageMaker/.env
       echo "model_s3_bucket=${var.model_s3_bucket}" >> /home/ec2-user/SageMaker/.env
       echo "inference_instance_type" = ${var.inference_instance_type} >> /home/ec2-user/SageMaker/.env
       echo "inference_instance_count" = ${var.inference_instance_count} >> /home/ec2-user/SageMaker/.env
       echo "ecr_repo_uri" = ${var.ecr_repo_uri} >> /home/ec2-user/SageMaker/.env
       echo "tuning_metric" = ${var.tuning_metric} >> /home/ec2-user/SageMaker/.env
     EOL
  )
}
