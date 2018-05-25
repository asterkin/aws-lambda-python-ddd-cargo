"""Estimate cargo next handling activity based on itinerary and the most recent event."""

from collections import defaultdict
from nahash import *
from common import findLeg

def Event(eventType, location=None, voyageId=None, completionTime=None):
    return dropNone({'eventType': eventType, 'location': location, 'voyageId': voyageId, 'completionTime': completionTime})

def expectUnload(lastEvent, itinerary):
    leg, _ = findLeg(lastEvent, itinerary)

    if leg == None: return Event('NO_ACTIVITY')
    return Event('UNLOAD', leg.unloadLocation, leg.voyageId, leg.unloadTime)

def expectLoad(leg):
    return Event('LOAD', leg.loadLocation, leg.voyageId, leg.loadTime)
    
def expectLoadOrClaim(lastEvent, itinerary):
    leg, it = findLeg(lastEvent, itinerary)
    
    if leg == None: return Event('NO_ACTIVITY') 
    nextLeg = next(it, None)
    if nextLeg == None: return Event('CLAIM', leg.unloadLocation)
    return expectLoad(nextLeg)

def expectLoadAtOrigin(lastEvent, itinerary):
    return expectLoad(itinerary[0])

def default():
    return lambda lastEvent, itinerary: Event('NO_ACTIVITY')

expect = defaultdict(
    default, [
    ('LOAD',    expectUnload),
    ('UNLOAD',  expectLoadOrClaim),
    ('RECEIVE', expectLoadAtOrigin)
])

def nextExpectedEvent(lastEvent, itinerary):
    return expect[lastEvent.eventType](lastEvent, itinerary)

def lambda_handler(input, context):
    inpjs = jso(input)
    return nextExpectedEvent(inpjs.lastEvent, inpjs.itinerary)