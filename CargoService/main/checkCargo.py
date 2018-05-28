""" Check whether cargo referece is correct."""

import boto3
import os
from CargoService import CARGO

def resources():
    return [
        {'ref': 'Cargo', 'ops': ['dynamodb:GetItem']}
    ]

dynamodb = boto3.resource('dynamodb')
dbname = os.getenv('Cargo')
table = dynamodb.Table(dbname if dbname else 'ignore') #required for samgen

def checkCargo(cargo):
    return 'OK' if 'Item' in table.get_item(Key={CARGO:cargo},ProjectionExpression=CARGO) else 'CARGO_NOT_FOUND'

def lambda_handler(event, context):
    return checkCargo(event['cargo']) if 'cargo' in event else 'CARGO_REFERENCE_IS_MISSING'
