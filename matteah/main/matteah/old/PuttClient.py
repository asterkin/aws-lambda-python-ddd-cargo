from matteah import RepositoryClient

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

