"""Calculate cargo delivery status based on itinerary and the most recent event."""

from lib.Itinerary import Itinerary
import CargoHandlingEvent

def expected_at_interim_leg(last_event, itinerary):
    leg = itinerary.find(last_event)
    return (True, leg.is_on_schedule(last_event)) if leg else (False, '')

def expected_at_edge(last_event, leg):
    expected = leg.is_expected(last_event)
    return (expected, leg.is_on_schedule(last_event) if expected else '')

def expected_at_first_leg(last_event, itinerary):
    return expected_at_edge(last_event, itinerary.first())

def expected_at_final_leg(last_event, itinerary):
    return expected_at_edge(last_event, itinerary.last())

def default(last_event, itinerary):
    return (False, '')

def expect(last_event, itinerary):
    return {
        CargoHandlingEvent.RECEIVE: expected_at_first_leg,
        CargoHandlingEvent.LOAD:    expected_at_interim_leg,
        CargoHandlingEvent.UNLOAD:  expected_at_interim_leg,
        CargoHandlingEvent.CUSTOMS: expected_at_final_leg,
        CargoHandlingEvent.CLAIM:   expected_at_final_leg
    }.get(last_event.event_type, default)(last_event, itinerary)

def calculate_delivery_status(last_event, itinerary):
    if not itinerary: return 'UNKNOWN'
    (expected, on_schedule) = expect(last_event, Itinerary(itinerary))
    return on_schedule if expected else 'MISDIRECTED'
