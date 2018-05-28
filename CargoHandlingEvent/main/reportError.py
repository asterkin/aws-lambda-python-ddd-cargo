"""Report CargoHandlingEventError for further investigation."""

import json

def lambda_handler(input, context):
    print(json.dumps(input))
