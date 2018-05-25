from collections import defaultdict
from nahash import *

def findLeg(lastEvent, itinerary):
    loc = lastEvent.eventType.lower() + 'Location'
    return find(lambda leg: lastEvent.location == leg[loc] and lastEvent.voyageId == leg.voyageId, itinerary)
