from matteah import RepositoryClient

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
