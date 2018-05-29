"""Retrieve Cargo specification for the given id."""

import boto3
import os
from CargoService import CARGO
import DecimalEncoder

def resources():
    return [
        {'ref': 'Specification', 'ops': ['dynamodb:GetItem']}
    ]

dynamodb = boto3.resource('dynamodb')
dbname = os.getenv('Specification')
table = dynamodb.Table(dbname if dbname else 'ignore') #required for samgen

def getSpecification(cargo):
    result = table.get_item(Key={CARGO:cargo})
    return result['Item'] if 'Item' in result else 'CARGO_SPECIFICATION_NOT_FOUND'

def lambda_handler(event, context):
    return getSpecification(event['cargo'])
