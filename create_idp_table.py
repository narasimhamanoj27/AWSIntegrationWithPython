import boto3

dyn_resource = boto3.resource('dynamodb', region_name='us-east-1')


def create_idp_table():
    idp_table_name = 'IdpCredentials'
    params = {
        'TableName': idp_table_name,
        'KeySchema': [
            {'AttributeName': 'api_name', 'KeyType': 'HASH'},
            {'AttributeName': 'idp_provider', 'KeyType': 'RANGE'}
        ],
        'AttributeDefinitions': [
            {'AttributeName': 'api_name', 'AttributeType': 'S'},
            {'AttributeName': 'idp_provider', 'AttributeType': 'S'}
        ],
        'ProvisionedThroughput': {
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    }

    dynamo_table = dyn_resource.create_table(**params)
    print(f"Creating {dynamo_table}...")
    dynamo_table.wait_until_exists()
    return dynamo_table


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    idp_table = create_idp_table()
    print(f"Created table.")
