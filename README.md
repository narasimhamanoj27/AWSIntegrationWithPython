# AWSIntegrationWithPython

# DynamoDB 

Creating a table for AWS integration of DynamoDB.
Table structure is as below.

Table IDP Credentials
Columns

* api_name | String | Primary Key
* idp_provider | String | Sort Key
* idp_url | String

Based on the above details we will be creating a Python Script to create the table and later insert the information into it.


```
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
```

Data insertion from Python script using boto3 package from AWS.


```
import boto3
import json

dyn_resource = boto3.resource('dynamodb', region_name='us-east-1')
idp_table = dyn_resource.Table('IdpCredentials')


def insert_idp_table_data(idp_data):
    for idp_item in idp_data:
        api_name = (idp_item['api_name'])
        idp_provider = idp_item['idp_provider']
        idp_url = idp_item['idp_url']
        print("Loading IDP Data: ", api_name, idp_provider, idp_url)
        idp_table.put_item(Item=idp_item)


if __name__ == '__main__':
    with open("content/idp_data.json") as idp_data_json:
        idp_info = json.load(idp_data_json)
    insert_idp_table_data(idp_info)
    print('Table data inserted..')
```


Data inside the DynamoDB table inside AWS Console.

