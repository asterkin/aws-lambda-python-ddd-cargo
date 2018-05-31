"""Generic Repository class. Kinda poor-main ORM"""

dbResTemplate = """
    $NAME:
        Type: AWS::DynamoDB::Table
        Properties: 
            AttributeDefinitions:$ATTRIBUTES
            KeySchema:$KEYS
            ProvisionedThroughput: 
                ReadCapacityUnits: 5
                WriteCapacityUnits: 5
"""
#TBD parametrized throughput

resActionsTemplate = """
                      Action:$ACTIONS
                      Resource: !GetAtt $RESOURCE.Arn
"""
resActionTemplate = """
                        - '$ACTION'
"""

import boto3
import os

def attribute(attr):
    return """
                - AttributeName: $NAME
                  AttributeType: $TYPE""".replace('$NAME', attr['name']).replace('$TYPE', attr['type']) if attr else ''

def key(attr, keyType):
    return """
                - AttributeName: $NAME
                  KeyType: $TYPE""".replace('$NAME', attr['name']).replace('$TYPE', keyType) if attr else ''

class Repository:
    def __init__(self, name, **kwargs):
        self.name = name
        self.hashKey  = kwargs.get('hashKey')
        self.rangeKey = kwargs.get('rangeKey', None)
    def __str__(self):
        return dResTemplate.replace('$NAME', self.name).replace('$ATTRIBUTES', self.attributes()).replace('$KEYS', self.keys())
    def attributes(self):
        return attribute(self.hashKey) + attribute(self.rangeKey)
    def keys(self):
        return key(self.hashKey, 'HASH') + key(self.rangeKey, 'RANGE')


                    

