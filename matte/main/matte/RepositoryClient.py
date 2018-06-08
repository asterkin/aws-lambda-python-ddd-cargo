from .Client import Client
import boto3
import os

resActionsTemplate = """
                      Action:$ACTIONS
                      Resource: !GetAtt $RESOURCE.Arn
"""
resActionTemplate = """
                        - '$ACTION'
"""

class RepositoryClient(Client):
    def __init__(self, repository, *actions):
        Client.__init__(self, repository.name)
        self.dynamodb = boto3.resource('dynamodb')
        dbname = os.getenv(self.name)
        self.table = self.dynamodb.Table(dbname) if dbname else None #required for samgen
        self.hashKey = repository.hashKey
        self.rangeKey = repository.rangeKey
        self.actions = actions
    def __str__(self):
        return resActionsTemplate.replace('$ACTIONS', ''.join(map(lambda a: resActionTemplate
                .replace('$ACTION', 'dynamodb:'+a), self.actions))).replace('$RESOURCE', self.name)
