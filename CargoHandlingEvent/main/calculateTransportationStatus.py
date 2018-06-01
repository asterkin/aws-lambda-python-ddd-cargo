"""Convert cargo handling evet type into transportation status."""

import CargoHandlingEvent

def calculateTransportationStatus(event):
    return {
        None:                        'NOT_RECEIVED',
        CargoHandlingEvent.LOAD:     'ONBOARD_CARRIER',
        CargoHandlingEvent.UNLOAD:   'IN_PORT',
        CargoHandlingEvent.RECEIVE:  'IN_PORT',
        CargoHandlingEvent.CUSTOMS:  'IN_PORT',
        CargoHandlingEvent.CLAIM:    'CLAIMED'
    }.get(event.eventType, 'UNKNOWN')


