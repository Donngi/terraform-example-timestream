output "timestream_database_name" {
  value = aws_timestreamwrite_database.sample.id
}
output "timestream_table_name" {
  value = aws_timestreamwrite_table.sample.table_name
}
