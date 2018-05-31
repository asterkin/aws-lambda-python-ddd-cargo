class RepositoryClient:
    def __init__(self, repository, *actions):
        self.dynamodb = boto3.resource('dynamodb')
        dbname = os.getenv(repository.name)
        this.table = dynamodb.Table(dbname) if dbname else None #required for samgen
        this.hashKey = repository.hashKey
        this.rangeKey = repository.rangeKey
        this.actions = actions
    def __str__(self):
        return resActionsTemplate.replace('$ACTIONS', ''.join(map(lambda a: resActionTemplate
                .replace('$ACTION', a), self.actions))).replace('$RESOURCE', self.name)

