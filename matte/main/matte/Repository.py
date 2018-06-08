"""Generic Repository class. Kinda poor-main ORM"""

from .Resource import Resource
from .GetClient import GetClient
from .PutClient import PutClient
from .QueryClient import QueryClient
import boto3

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

def attribute(attr):
    return """
                - AttributeName: $NAME
                  AttributeType: $TYPE""".replace('$NAME', attr['name']).replace('$TYPE', attr['type']) if attr else ''

def key(attr, keyType):
    return """
                - AttributeName: $NAME
                  KeyType: $TYPE""".replace('$NAME', attr['name']).replace('$TYPE', keyType) if attr else ''

def keyType(t):
    return {
        int : 'N',
        str : 'S'
    }.get(t)

def keySpec(key):
    if not key: return None
    assert(len(key.keys()) == 1)
    name = next(iter(key.keys()))
    return {'name': name, 'type': keyType(key[name])}

class Repository(Resource):
    def __init__(self, name, **kwargs):
        Resource.__init__(self, name)
        self.hashKey  = keySpec(kwargs.get('hashKey'))
        self.rangeKey = keySpec(kwargs.get('rangeKey', None))
    def __str__(self):
        return dbResTemplate.replace('$NAME', self.name).replace('$ATTRIBUTES', self.__attributes__()).replace('$KEYS', self.__keys__())
    def __attributes__(self):
        return attribute(self.hashKey) + attribute(self.rangeKey)
    def __keys__(self):
        return key(self.hashKey, 'HASH') + key(self.rangeKey, 'RANGE')
    def get_client(self):
        return GetClient(self)
    def put_client(self):
        return PutClient(self)
    def query_client(self):
        return QueryClient(self)

