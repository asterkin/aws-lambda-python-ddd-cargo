"""Estimate cargo next handling activity based on itinerary and the most recent event."""

from lib.Itinerary import Itinerary
import CargoHandlingEvent

def expect_unload(last_event, itinerary):
    return itinerary.find(last_event).unload()
    
def expect_load_or_claim(last_event, itinerary):
    leg = itinerary.find(last_event)
    if leg == None: return CargoHandlingEvent.no_activity()
    next_leg = next(leg)

    return next_leg.load() if next_leg else leg.claim()

def expect_load_at_origin(last_event, itinerary):
    return itinerary.first().load()

def default(last_event, itinerary):
    return CargoHandlingEvent.no_activity()

def expect(last_event, itinerary):
    return {
        CargoHandlingEvent.LOAD:    expect_unload,
        CargoHandlingEvent.UNLOAD:  expect_load_or_claim,
        CargoHandlingEvent.RECEIVE: expect_load_at_origin
    }.get(last_event.event_type, default)(last_event, itinerary)

def calculate_next_activity(last_event, itinerary):
    return expect(last_event, Itinerary(itinerary)) if itinerary else CargoHandlingEvent.no_activity()

