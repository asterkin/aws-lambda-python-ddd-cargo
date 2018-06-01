"""Check whether Voyage reference is required and if so, is supplied."""

import CargoHandlingEvent

def voyage_required(event_type):
    return event_type in {CargoHandlingEvent.LOAD, CargoHandlingEvent.UNLOAD}
    
def check_voyage(event):
    if not event.event_type: return 'EVENT_TYPE_IS_MISSING'
    elif voyage_required(event.event_type):
        return'OK' if event.voyage else 'VOYAGE_REF_IS_MISSING'
    else:
        return 'OK' if not event.voyage else 'UNEXPECTED_VOYAGE_REFERENCE'
