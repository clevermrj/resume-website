import json
import boto3

dynamodb = boto3.client('dynamodb')
TableName = 'my-resume-table'

def lambda_handler(event, context):
    
    '''
    data = client.get_item(
        TableName='my-resume-table',
        Key = {
            'VisitorCount': {'S': 'view-count'}
        }
    )
    '''
    
    #data['Item']['Visits']['N'] = str(int(data['Item']['Visits']['N']) + 1)
    
    response = dynamodb.update_item(
        TableName='my-resume-table',
        Key = {
            'VisitorCount': {'S': 'view-count'}
        },
        UpdateExpression = 'ADD Quantity :inc',
        ExpressionAttributeValues = {":inc" : {"N": "1"}},
        ReturnValues = 'UPDATED_NEW'
        )
        
    value = response['Attributes']['Quantity']['N']
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(str(value))
    }
