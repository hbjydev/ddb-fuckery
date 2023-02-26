import boto3
from entities import Tenant, Member

dynamodb = boto3.client("dynamodb", endpoint_url='http://localhost:8000/')

TENANT_ID = "clelkd4zn00012v6kr5wj9b1p"


def fetch_tenant_and_users(tenant_id):
    resp = dynamodb.query(
        TableName='datacore',
        KeyConditionExpression="PK = :pk AND SK BETWEEN :metadata AND :users",
        ExpressionAttributeValues={
            ":pk": { "S": "TNNT#{}".format(tenant_id) },
            ":metadata": { "S": "#METADATA#{}".format(tenant_id) },
            ":users": { "S": "USER$" },
        },
        ScanIndexForward=True
    )
    tenant = Tenant(resp['Items'][0])
    tenant.users = [Member(item) for item in resp['Items'][1:]]

    return tenant


tenant = fetch_tenant_and_users(TENANT_ID)

print(tenant)
for user in tenant.users:
    print(user)