from typing import List


class TimeStreamDataWriter:
    client = None

    def __init__(self, client) -> None:
        self.client = client

    def write_records(self, database_name: str, table_name: str, records: List[dict], common_attributes: List[dict] = None,):
        if self.client is None:
            raise Exception('client is not set')

        if common_attributes is None:
            response = self.client.write_records(
                DatabaseName=database_name,
                TableName=table_name,
                Records=records
            )
            return response
        else:
            response = self.client.write_records(
                DatabaseName=database_name,
                TableName=table_name,
                CommonAttributes=common_attributes,
                Records=records
            )
            return response
