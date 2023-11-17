resource "aws_s3_bucket" "module-registry" {
  bucket = var.bucket_name
}

resource "aws_s3_bucket_policy" "allow_access_to_tfstate_role" {
  bucket = aws_s3_bucket.module-registry.id
  policy = data.aws_iam_policy_document.allow_access_to_tfstate_role.json
}

data "aws_iam_policy_document" "allow_access_to_tfstate_role" {
  statement {
    principals {
      type        = "AWS"
      identifiers = ["arn:aws:iam::283211881821:role/TerraformNonprodTFStateAccess"]
    }

    actions = [
      "s3:GetObject",
      "s3:GetBucketLocation",
      "s3:ListBucket"
    ]

    resources = [
      aws_s3_bucket.module-registry.arn,
      "${aws_s3_bucket.module-registry.arn}/*"
    ]
  }
}
