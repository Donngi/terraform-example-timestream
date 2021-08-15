module "timestream" {
  source = "../../module/timestream"
}

module "lambda" {
  source                   = "../../module/lambda"
  timestream_database_name = module.timestream.timestream_database_name
  timestream_table_name    = module.timestream.timestream_table_name
}
