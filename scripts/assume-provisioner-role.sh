#!/bin/bash

export $(printf "AWS_ACCESS_KEY_ID=%s AWS_SECRET_ACCESS_KEY=%s AWS_SESSION_TOKEN=%s" \
$(aws sts assume-role \
--role-arn arn:aws:iam::135544376709:role/NonprodProvisionerRole \
--role-session-name moduleUploadSession \
--query "Credentials.[AccessKeyId,SecretAccessKey,SessionToken]" \
--output text))
