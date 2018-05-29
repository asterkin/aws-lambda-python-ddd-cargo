"""Store Location Definition."""

import boto3
import os

def resources():
    return [
        {'ref': 'Location', 'ops': ['dynamodb:PutItem']}
    ]

dynamodb = boto3.resource('dynamodb')
dbname = os.getenv('Location')
table = dynamodb.Table(dbname if dbname else 'ignore') #required for samgen

def putItinerary(location):
    item = { #security measure not to flush arbitrary object into DB
        'location': location['location'],
        'name': location['name'] 
    }
    table.put_item(Item=item) #TODO: error handling, write capacity
    return 'OK'

def lambda_handler(input, context):
    return putLocation(input)
