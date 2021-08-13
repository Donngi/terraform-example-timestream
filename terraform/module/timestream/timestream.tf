resource "aws_timestreamwrite_database" "sample" {
  database_name = "SampleDatabase"
}

resource "aws_timestreamwrite_table" "sample" {
  database_name = aws_timestreamwrite_database.sample.database_name
  table_name    = "SampleTable"

  retention_properties {
    magnetic_store_retention_period_in_days = 30
    memory_store_retention_period_in_hours  = 1
  }
}
