from matteah.RepositoryClient import RepositoryClient

class GetClient(RepositoryClient):
    def __init__(self, repository):
        RepositoryClient.__init__(self, repository, 'GetItem')
    def has_item(key):
        return 'Item' in self.table.get_item(Key={self.hashKay:key},ProjectionExpression=self.hashKey)
    def get_item(key):
        res = self.table.get_item(Key={self.hashKay:key})
        return res['Item'] if 'Item' in res else None

