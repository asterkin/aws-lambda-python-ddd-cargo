"""Retrieve Cargo itinerary for the given id."""

import boto3
import os
from Cargo import CARGO
import DecimalEncoder

def resources():
    return [
        {'ref': 'Itinerary', 'ops': ['dynamodb:GetItem']}
    ]

dynamodb = boto3.resource('dynamodb')
dbname = os.getenv('Specification')
table = dynamodb.Table(dbname if dbname else 'ignore') #required for samgen

def getItinerary(cargo):
    result = table.get_item(Key={CARGO:cargo})
    if not 'Item' in result: return 'CARGO_ITINERARY_NOT_FOUND'
    return result['Item']['schedule']

def lambda_handler(event, context):
    return getItinerary(event['cargo'])
