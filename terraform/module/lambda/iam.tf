resource "aws_iam_role" "sample" {
  name = "SampleLambdaTimeStreamRole"

  assume_role_policy = jsonencode(
    {
      "Version" : "2012-10-17",
      "Statement" : [
        {
          "Action" : "sts:AssumeRole",
          "Principal" : {
            "Service" : "lambda.amazonaws.com"
          },
          "Effect" : "Allow",
        }
      ]
    }
  )
}

resource "aws_iam_policy" "sample" {
  name = "SampleLambdaTimeStreamRolePolicy"

  policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Effect" : "Allow",
        "Action" : "timestream:ListTables",
        "Resource" : "arn:aws:timestream:*:${data.aws_caller_identity.current.account_id}:database/*"
      },
      {
        "Effect" : "Allow",
        "Action" : [
          "timestream:ListMeasures",
          "timestream:WriteRecords"
        ],
        "Resource" : "arn:aws:timestream:*:${data.aws_caller_identity.current.account_id}:database/*/table/*"
      },
      {
        "Effect" : "Allow",
        "Action" : "timestream:ListDatabases",
        "Resource" : "*"
      },
      {
        "Effect" : "Allow",
        "Action" : "timestream:DescribeEndpoints",
        "Resource" : "*"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "sample" {
  role       = aws_iam_role.sample.name
  policy_arn = aws_iam_policy.sample.arn
}
