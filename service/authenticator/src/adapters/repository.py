from typing import Dict

from botocore.exceptions import ClientError

from authenticator.src.domain import model


class DynamoDBError(Exception):
    def __init__(self, message: str):
        self.context = {'httpCode': 500, 'exceptionType': self.__class__.__name__}
        super().__init__(message)


class UsersRepository:
    def __init__(self, resource, table_name: str):
        self.session = resource
        self.table_name = table_name
        self.table = self.session.Table(self.table_name)
        self.read_capacity_units = 10
        self.write_capacity_units = 10
        self.key = 'email'

    def add(self, item: model.User) -> Dict:
        return self.table.put_item(Item=dict(item))

    def update(self, item: model.User) -> Dict:
        return self.add(item=item)

    def create_table(self) -> Dict:
        try:
            table = self.session.create_table(
                TableName=self.table_name,
                KeySchema=[
                    {
                        'AttributeName': self.key,
                        'KeyType': 'HASH'  # Partition key
                    },
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': self.key,
                        'AttributeType': 'S'
                    },
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': self.read_capacity_units,
                    'WriteCapacityUnits': self.write_capacity_units
                }
            )
            return table
        except ClientError as error:
            raise DynamoDBError(error.response['Error']['Message'])
