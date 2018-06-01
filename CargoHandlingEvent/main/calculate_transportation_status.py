"""Convert cargo handling event type into transportation status."""

import CargoHandlingEvent

def calculate_transportation_status(last_event):
    return {
        None:                        'NOT_RECEIVED',
        CargoHandlingEvent.LOAD:     'ONBOARD_CARRIER',
        CargoHandlingEvent.UNLOAD:   'IN_PORT',
        CargoHandlingEvent.RECEIVE:  'IN_PORT',
        CargoHandlingEvent.CUSTOMS:  'IN_PORT',
        CargoHandlingEvent.CLAIM:    'CLAIMED'
    }.get(last_event.event_type, 'UNKNOWN')


