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
