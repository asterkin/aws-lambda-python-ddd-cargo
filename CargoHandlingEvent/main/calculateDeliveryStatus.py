"""Calculate cargo delivery status based on itinerary and the most recent event."""

from lib.Itinerary import Itinerary
import CargoHandlingEvent

def expectedAtInterimLeg(lastEvent, itinerary):
    leg = itinerary.find(lastEvent)
    return (False, '') if leg == None else (True, leg.isOnSchedule(lastEvent))

def expectedAtEdge(lastEvent, leg):
    expected = leg.isExpected(lastEvent)
    return (expected, leg.isOnSchedule(lastEvent) if expected else '')

def expectedAtFirstLeg(lastEvent, itinerary):
    return expectedAtEdge(lastEvent, itinerary.first())

def expectedAtFinalLeg(lastEvent, itinerary):
    return expectedAtEdge(lastEvent, itinerary.last())

def default(lastEvent, itinerary):
    return (False, '')

def expect(lastEvent, itinerary):
    return {
        CargoHandlingEvent.RECEIVE: expectedAtFirstLeg,
        CargoHandlingEvent.LOAD:    expectedAtInterimLeg,
        CargoHandlingEvent.UNLOAD:  expectedAtInterimLeg,
        CargoHandlingEvent.CUSTOMS: expectedAtFinalLeg,
        CargoHandlingEvent.CLAIM:   expectedAtFinalLeg
    }.get(lastEvent.eventType, default)(lastEvent, itinerary)

def calculateDeliveryStatus(lastEvent, itinerary):
    if not itinerary: return 'UNKNOWN'
    (expected, onSchedule) = expect(lastEvent, Itinerary(itinerary))
    return onSchedule if expected else 'MISDIRECTED'
