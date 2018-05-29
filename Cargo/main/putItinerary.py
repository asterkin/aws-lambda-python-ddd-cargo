"""Store Cargo Itinerary."""

import boto3
import os
from Cargo import CARGO

def resources():
    return [
        {'ref': 'Itinerary', 'ops': ['dynamodb:PutItem']}
    ]

dynamodb = boto3.resource('dynamodb')
dbname = os.getenv('Specification')
table = dynamodb.Table(dbname if dbname else 'ignore') #required for samgen

def putItinerary(itinerary):
    item = { #security measure not to flush arbitrary object into DB
        'cargo': itinerary['cargo'],
        'schedule': itinerary['schedule'] #TODO: shall I check every array element
    }
    table.put_item(Item=item) #TODO: error handling, write capacity
    return 'OK'

def lambda_handler(input, context):
    return putItinerary(input)
