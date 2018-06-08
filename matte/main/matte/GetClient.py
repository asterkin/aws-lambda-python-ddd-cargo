from .RepositoryClient import RepositoryClient
from .DecimalEncoder import DecimalEncoder

class GetClient(RepositoryClient):
    def __init__(self, repository):
        RepositoryClient.__init__(self, repository, 'GetItem')
    def has_item(self, key):
        return 'Item' in self.table.get_item(Key={self.hashKey['name']:key},ProjectionExpression=self.hashKey['name'])
    def get_item(self, key):
        res = self.table.get_item(Key={self.hashKey['name']:key})
        return res['Item'] if 'Item' in res else None
