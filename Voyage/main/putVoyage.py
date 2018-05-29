"""Store Voyage Schedule."""

import boto3
import os

def resources():
    return [
        {'ref': 'Voyage', 'ops': ['dynamodb:PutItem']}
    ]

dynamodb = boto3.resource('dynamodb')
dbname = os.getenv('Voyage')
table = dynamodb.Table(dbname if dbname else 'ignore') #required for samgen

def putVoyage(voyage):
    item = { #security measure not to flush arbitrary object into DB
        'voyage': voyage['voyage'],
        'voyage': itinerary['voyage'] #TODO: shall I check every array element
    }
    table.put_item(Item=item) #TODO: error handling, write capacity
    return 'OK'

def lambda_handler(input, context):
    return putVoyage(input)
