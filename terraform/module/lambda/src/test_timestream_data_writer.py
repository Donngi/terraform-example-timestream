import pytest
import boto3
from botocore.stub import Stubber
from timestream_data_writer import TimeStreamDataWriter
import os

os.environ['AWS_ACCESS_KEY_ID'] = 'DUMMY_VALUE'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'DUMMY_VALUE'
os.environ['AWS_DEFAULT_REGION'] = 'ap-northeast-1'
os.environ['AWS_DEFAULT_REGION'] = 'ap-northeast-1'


def test_write_records_success():
    client = boto3.client('timestream-write')
    stubber = Stubber(client)
    stubber.add_response('write_records', {'ResponseMetadata':
                                           {
                                               'HTTPStatusCode': 200
                                           }
                                           })
    stubber.activate()

    # Given
    database_name = 'test_database'
    table_name = 'test_table'
    records = [
        {
            'Dimensions': [
                {
                    'Name': 'hoge',
                    'Value': 'fuga',
                    'DimensionValueType': 'VARCHAR'
                },
            ],
            'MeasureName': 'status',
            'MeasureValue': 'ok',
            'MeasureValueType': 'VARCHAR',
            'Time': '1234',
            'TimeUnit': 'MILLISECONDS',
            'Version': 1234
        },
    ]

    # When
    timestream_writer = TimeStreamDataWriter(client)
    got = timestream_writer.write_records(
        database_name=database_name, table_name=table_name, records=records)

    # Then
    assert got['ResponseMetadata']['HTTPStatusCode'] == 200


def test_write_records_failure():
    client = boto3.client('timestream-write')
    stubber = Stubber(client)
    stubber.add_client_error('write_records', 'want error')
    stubber.activate

    # Given
    database_name = 'test_database'
    table_name = 'test_table'
    records = [
        {
            'Dimensions': [
                {
                    'Name': 'hoge',
                    'Value': 'fuga',
                    'DimensionValueType': 'VARCHAR'
                },
            ],
            'MeasureName': 'status',
            'MeasureValue': 'ok',
            'MeasureValueType': 'VARCHAR',
            'Time': '1234',
            'TimeUnit': 'MILLISECONDS',
            'Version': 1234
        },
    ]

    timestream_writer = TimeStreamDataWriter(client)

    with pytest.raises(Exception) as e:
        # When
        timestream_writer.write_records(
            database_name=database_name, table_name=table_name, records=records)

        # Then
        assert str(e.value) == 'want error'
