"""Estimate cargo next handling activity based on itinerary and the most recent event."""

from lib.Itinerary import Itinerary
import CargoHandlingEvent

def expectUnload(lastEvent, itinerary):
    return itinerary.find(lastEvent).unload()
    
def expectLoadOrClaim(lastEvent, itinerary):
    leg = itinerary.find(lastEvent)
    if leg == None: return CargoHandlingEvent.no_activity()
    nextLeg = next(leg)

    return leg.load() if nextLeg else leg.claim()

def expectLoadAtOrigin(lastEvent, itinerary):
    return itinerary.first().load(lastEvent.cargo)

def default(lastEvent, itinerary):
    return CargoHandlingEvent.no_activity()

def expect(lastEvent, itinerary):
    return {
        CargoHandlingEvent.LOAD:    expectUnload,
        CargoHandlingEvent.UNLOAD:  expectLoadOrClaim,
        CargoHandlingEvent.RECEIVE: expectLoadAtOrigin
    }.get(lastEvent.eventType, default)(lastEvent, itinerary)

def calculateNextActivity(lastEvent, itinerary):
    return expect(lastEvent, Itinerary(itinerary)) if itinerary else CargoHandlingEvent.no_activity()

