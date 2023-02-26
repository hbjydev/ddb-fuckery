import boto3
from botocore.config import Config

dynamodb = boto3.client(
    "dynamodb",
    endpoint_url='http://localhost:8000',
)

try:
    table = dynamodb.create_table(
        TableName='datacore',
        AttributeDefinitions=[
            {
                "AttributeName": "PK",
                "AttributeType": "S"
            },
            {
                "AttributeName": "SK",
                "AttributeType": "S"
            }
        ],
        KeySchema=[
            {
                "AttributeName": "PK",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "SK",
                "KeyType": "RANGE"
            }
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 1,
            "WriteCapacityUnits": 1,
        }
    )
except Exception as e:
    print("Could not create table. Error:")
    print(e)
