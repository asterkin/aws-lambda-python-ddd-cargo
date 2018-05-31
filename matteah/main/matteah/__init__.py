"""Find in list using a general predicate. Seems to be missing in Python"""
def find(p, xs):
    it = iter(xs)
    for v in it:
        if(p(v)): return (v, it)
    return (None, it)

"""Drop all None values in a dict."""
def dropNone(d):
    return {k:v for k,v in d.items() if v is not None}

#I do not like this monolith, but my knowledge of Python module structure is limitted

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

class RepositoryClient:
    def __init__(self, repository, *actions):
        self.name = repository.name
        self.dynamodb = boto3.resource('dynamodb')
        dbname = os.getenv(self.name)
        self.table = dynamodb.Table(dbname) if dbname else None #required for samgen
        self.hashKey = repository.hashKey
        self.rangeKey = repository.rangeKey
        self.actions = actions
    def __str__(self):
        return resActionsTemplate.replace('$ACTIONS', ''.join(map(lambda a: resActionTemplate
                .replace('$ACTION', a), self.actions))).replace('$RESOURCE', self.name)

"""Helper class to convert a DynamoDB item to JSON."""

import json

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

class GetClient(RepositoryClient):
    def __init__(self, repository):
        RepositoryClient.__init__(self, repository, 'GetItem')
    def has_item(key):
        return 'Item' in self.table.get_item(Key={self.hashKay:key},ProjectionExpression=self.hashKey)
    def get_item(key):
        res = self.table.get_item(Key={self.hashKay:key})
        return res['Item'] if 'Item' in res else None

class PutClient(RepositoryClient):
    def __init__(self, repository):
        RepositoryClient.__init__(self, repository, 'PutItem')
        self.unique = 'attribute_not_exists(%s)' % hashKey
        if rangeKey: self.unique += 'AND attribute_not_exists(%s)' % rangeKey
    def put_item(item, unique=True):
        try:
            self.table.put_item(
                Item = item,
                ConditionExpression = self.unique if unique else None
            )
            return "OK"
        except ClientError as e:
            if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
                return 'DUPLICATE'
            raise

class QueryClient(RepositoryClient):
    def __init__(self, name, hashKey, rangeKey):
        RepositoryClient.__init__(self, name, hashKey, 'Query')
    def get_last(self, key):
        result = table.query(
            KeyConditionExpression=Key(self.hashKey).eq(key),
            Limit = 1,
            ScanIndexForward = False
        )['Items']
        return result[0] if len(result) == 1 else 'NOT_FOUND'

    

        
