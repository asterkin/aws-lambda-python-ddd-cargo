"""Convert cargo handling evet type into transportation status."""

from collections import defaultdict
from nahash import jso

status = defaultdict(
    lambda : 'UNKNOWN',[
        (None, 'NOT_RECEIVED'),
        ('LOAD', 'ONBOARD_CARRIER'),
        ('UNLOAD',  'IN_PORT'),
        ('RECEIVE', 'IN_PORT'),
        ('CUSTOMS', 'IN_PORT'),
        ('CLAIM',   'CLAIMED')

])

def lambda_handler(input, context):
    return status[jso(input).eventType]

