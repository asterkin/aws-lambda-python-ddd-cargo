"""Store CargoHandlingEvent record in database"""

import boto3
from botocore.exceptions import ClientError
import time
import os

dynamodb = boto3.resource('dynamodb')
dbname = os.getenv('CargoHandlingEvent')
table = dynamodb.Table(dbname if dbname else 'ignore') #required for samgen

def lambda_handler(event, context):
    try:
        table.put_item(
            Item= {
                #this is do mostly for security reasons - not to put into DB unchecked record
                'cargo':            event['cargo'],
                'completionTime':   event['completionTime'],
                'registrationTime': int(time.time()*1000),
                'voyage':           event['voyage'],
                'eventType':        event['eventType'],
                'location':         event['location']
            },
            ConditionExpression = 'attribute_not_exists(cargo) AND attribute_not_exists(completionTime)'
        )
        return "OK"
    except ClientError as e:
        if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
            return 'DUPLICATE'
        raise
    