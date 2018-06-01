"""Check whether Voyage reference is required and if so, is supplied."""

import CargoHandlingEvent

def voyageRequired(eventType):
    return eventType in {CargoHandlingEvent.LOAD, CargoHandlingEvent.UNLOAD}
    
def checkVoyage(event):
    if not event.eventType: return 'EVENT_TYPE_IS_MISSING'
    elif voyageRequired(event.eventType):
        return'OK' if event.voyage else 'VOYAGE_REF_IS_MISSING'
    else:
        return 'OK' if not event.voyage else 'UNEXPECTED_VOYAGE_REFERENCE'
