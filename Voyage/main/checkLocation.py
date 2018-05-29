""" Check whether location referece is correct."""

import boto3
import os

def resources():
    return [
        {'ref': 'Location', 'ops': ['dynamodb:GetItem']}
    ]

dynamodb = boto3.resource('dynamodb')
dbname = os.getenv('Location')
table = dynamodb.Table(dbname if dbname else 'ignore') #required for samgen

def checkLocation(location):
    return 'OK' if 'Item' in table.get_item(Key={'location': location},ProjectionExpression='location') else 'LOCATION_NOT_FOUND'

def lambda_handler(event, context):
    return checkLocation(event['location']) if 'location' in event else 'LOCATION_REFERENCE_IS_MISSING'
