from matte import find
from lib.Leg import Leg, expected_event
    
class ItineraryObject:
    def __init__(self, schedule):
        self.schedule = schedule
    def find(self, event):
        return Leg(find(expected_event(event), self.schedule))
    def first(self):
        it  = iter(self.schedule)
        l = next(it, None)
        return Leg((l, it))
    def last(self):
        return Leg((self.schedule[-1], iter([])))

def Itinerary(schedule):
    return ItineraryObject(schedule) if schedule and len(schedule) > 0 else None
