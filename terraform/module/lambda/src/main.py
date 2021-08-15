import boto3
from timestream_data_writer import TimeStreamDataWriter
import os
import time
import traceback
import random


def lambda_handler(event, context):
    try:
        client = boto3.client('timestream-write')
        timestream_writer = TimeStreamDataWriter(client)

        database_name = os.getenv('TIMESTREAM_DATABASE_NAME')
        table_name = os.getenv('TIMESTREAM_TABLE_NAME')
        current_time_milliseconds = int(time.time()*1000)

        records = [
            {
                'Dimensions': [
                    {
                        'Name': 'lambda_function_name',
                        'Value': os.getenv('AWS_LAMBDA_FUNCTION_NAME'),
                        'DimensionValueType': 'VARCHAR'
                    },
                ],
                'MeasureName': 'status',
                'MeasureValue': random.choice(['on', 'off']),
                'MeasureValueType': 'VARCHAR',
                'Time': str(current_time_milliseconds),
                'TimeUnit': 'MILLISECONDS',
                'Version': current_time_milliseconds
            },
        ]

        res = timestream_writer.write_records(
            database_name=database_name,
            table_name=table_name,
            records=records
        )

        print(res)
        return {
            'statusCode': 200,
            'body': 'Success: {}'.format(res)

        }
    except Exception as e:
        print(traceback.format_exc())
        return {
            'statusCode': 500,
            'body': 'Error: {}'.format(e)
        }
