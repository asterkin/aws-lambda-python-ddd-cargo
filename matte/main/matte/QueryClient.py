from .RepositoryClient import RepositoryClient
from .DecimalEncoder import DecimalEncoder
from boto3.dynamodb.conditions import Key, Attr

class QueryClient(RepositoryClient):
    def __init__(self, repository):
        RepositoryClient.__init__(self, repository, 'Query')
    def get_last(self, key):
        result = self.table.query(
            KeyConditionExpression=Key(self.hashKey['name']).eq(key),
            Limit = 1,
            ScanIndexForward = False
        )['Items']
        return result[0] if len(result) == 1 else 'NOT_FOUND'
    
