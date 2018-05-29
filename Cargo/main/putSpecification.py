"""Store Cargo specification."""

import boto3
import os
from Cargo import CARGO

def resources():
    return [
        {'ref': 'Specification', 'ops': ['dynamodb:PutItem']}
    ]

dynamodb = boto3.resource('dynamodb')
dbname = os.getenv('Specification')
table = dynamodb.Table(dbname if dbname else 'ignore') #required for samgen

def putSpecification(specification):
    item = { #security measure not to flush arbitrary object into DB
        'cargo': specification['cargo'],
        'origin': specification['origin'],
        'destination': specification['destination'],
        'arrivalDeadline': specification['arrivalDeadline']
    }
    table.put_item(Item=item) #TODO: error handling, write capacity
    return 'OK'

def lambda_handler(input, context):
    return putSpecification(input)
