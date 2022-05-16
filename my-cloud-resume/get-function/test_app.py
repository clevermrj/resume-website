from app import *

import unittest
import boto3
import botocore
from moto import mock_dynamodb2

@mock_dynamodb2
class TestDynamoDB(unittest.TestCase):


    def setUp(self):
        #First check if table already exists. If it already exists that mean we connected to real AWS env and not mock.
        try:
             dynamodb = boto3.resource(
                "dynamodb")
             dynamodb.meta.client.describe_table(TableName='my-resume-table')
        except botocore.exceptions.ClientError:
            pass
        else:
            err = "{Table} should not exist.".format(Table='my-resume-table')
            raise EnvironmentError(err)
        
        table_name = 'my-resume-table'
        dynamodb = boto3.resource('dynamodb', 'us-east-1')

        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'VisitorCount',
                    'KeyType': 'HASH'
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'VisitorCount',
                    'AttributeType': 'S'
                },

            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

    def event():
        pass

    def context():
        pass
       
        self.assertTrue(int(resp_dict['body']) > 0);
        self.assertEqual(int(resp_dict['body']), 1);


if __name__ == '__main__':
    
    unittest.main()