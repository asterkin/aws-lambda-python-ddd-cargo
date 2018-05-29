"""Retrieve the most recent event for particular cargo"""

import boto3
import decimal
from boto3.dynamodb.conditions import Key, Attr
import os
import CargoHandlingEvent
import DecimalEncoder

def resources():
    return [
        {'ref': 'CargoHandlingEvents', 'ops': ['dynamodb:Query']}
    ]

dynamodb = boto3.resource('dynamodb')
dbname = os.getenv('CargoHandlingEvents')
table = dynamodb.Table(dbname if dbname else 'ignore') #required for samgen

def lambda_handler(event, context):
    result = table.query(
            KeyConditionExpression=Key('cargo').eq(event['cargo']),
            Limit = 1,
            ScanIndexForward = False
    )['Items']
    return result[0] if len(result) == 1 else 'NOT_FOUND'
