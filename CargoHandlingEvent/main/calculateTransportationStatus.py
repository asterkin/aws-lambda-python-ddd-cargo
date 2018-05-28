"""Convert cargo handling evet type into transportation status."""

from nahash import jso
import CargoHandlingEvent

def status(eventType):
    return {
        None:                        'NOT_RECEIVED',
        CargoHandlingEvent.LOAD:     'ONBOARD_CARRIER',
        CargoHandlingEvent.UNLOAD:   'IN_PORT',
        CargoHandlingEvent.RECEIVE:  'IN_PORT',
        CargoHandlingEvent.CUSTOMS:  'IN_PORT',
        CargoHandlingEvent.CLAIM:    'CLAIMED'
    }.get(eventType, 'UNKNOWN')

def lambda_handler(input, context):
    return status(jso(input).eventType)

