data "archive_file" "sample" {
  type        = "zip"
  source_dir  = "${path.module}/src"
  output_path = "${path.module}/upload/lambda.zip"
}

resource "aws_lambda_function" "sample" {
  filename      = data.archive_file.sample.output_path
  function_name = "SampleLambdaTimeStream"
  role          = aws_iam_role.sample.arn
  handler       = "main.lambda_handler"

  source_code_hash = data.archive_file.sample.output_base64sha256

  runtime = "python3.8"

  environment {
    variables = {
      TIMESTREAM_DATABASE_NAME = var.timestream_database_name
      TIMESTREAM_TABLE_NAME    = var.timestream_table_name
    }
  }

  timeout = 30
  publish = true
}
