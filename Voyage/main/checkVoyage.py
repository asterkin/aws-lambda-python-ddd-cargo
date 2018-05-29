""" Check whether voyage referece is correct."""

import boto3
import os

def resources():
    return [
        {'ref': 'Voyage', 'ops': ['dynamodb:GetItem']}
    ]

dynamodb = boto3.resource('dynamodb')
dbname = os.getenv('Voyage')
table = dynamodb.Table(dbname if dbname else 'ignore') #required for samgen

def checkLocation(voyage):
    return 'OK' if 'Item' in table.get_item(Key={'voyage': voyage},ProjectionExpression='voyage') else 'VOYAGE_NOT_FOUND'

def lambda_handler(event, context):
    return checkLocation(event['voyage']) if 'voyage' in event else 'VOYAGE_REFERENCE_IS_MISSING'
