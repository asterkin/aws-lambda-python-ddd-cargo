"""Calculate cargo delivery status based on itinerary and the most recent event."""

from collections import defaultdict
from nahash import jso
from common import findLeg

def againstSchedule(lastEvent, t):
    if lastEvent.completionTime < t:    return 'AHEAD_OF_SCHEDULE'  
    elif lastEvent.completionTime == t: return 'ON_SCHEDULE' 
    else:                               return 'BEHIND_SCHEDULE'

def expectedAndOnSchedule(lastEvent, itinerary):
    leg, _ = findLeg(lastEvent, itinerary)
    if leg == None: return (False, '')
    t = lastEvent.eventType.lower()+'Time'
    return (True, againstSchedule(lastEvent, leg[t]))

def receivedAtFirstLeg(lastEvent, itinerary):
    return (lastEvent.location == itinerary[0].loadLocation, againstSchedule(lastEvent, itinerary[0].loadTime))

def atLastLeg(lastEvent, itinerary):
    return(lastEvent.location == itinerary[-1].unloadLocation, againstSchedule(lastEvent, itinerary[-1].unloadTime))

def default():
    return lambda lastEvent, itinerary: (False, '')

expect = defaultdict(
    lambda : default, [
    ('RECEIVE', receivedAtFirstLeg),
    ('LOAD',    expectedAndOnSchedule),
    ('UNLOAD',  expectedAndOnSchedule),
    ('CUSTOMS', atLastLeg),
    ('CLAIM',   atLastLeg)
])

def deliveryStatus(lastEvent, itinerary):
    if(not itinerary or len(itinerary) == 0 ): return 'UNKNOWN'
    (expected, schedule) = expect[lastEvent.eventType](lastEvent, itinerary)
    return schedule if expected else 'MISDIRECTED'

def lambda_handler(input, context):    
    inpjs = jso(input)
    return deliveryStatus(inpjs.lastEvent, inpjs.itinerary)
