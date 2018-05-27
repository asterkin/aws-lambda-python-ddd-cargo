"""Encapsulates CargoHandlingEvent Repository and all relevant computations."""
from nahash import dropNone
from Repository import Repository

RECEIVE     = 'RECEIVE'
LOAD        = 'LOAD'
UNLOAD      = 'UNLOAD'
CLAIM       = 'CLAIM'
CUSTOMS     = 'CUSTOMS'
NO_ACTIVITY = 'NO_ACTIVITY'

CARGO = 'cargo'
TIMESTAMP = 'completionTime'

def resources():
    return [
        Repository('CargoHandlingEvents', hashKey = {'name': CARGO, 'type': 'S'}, rangeKey = {'name': TIMESTAMP, 'type': 'N'})
    ]

def CargoHandlingEvent(eventType, location=None, voyage=None, completionTime=None):
    return dropNone({'eventType': eventType, 'location': location, 'voyage': voyage, TIMESTAMP: completionTime})

def load(location, voyage, completionTime):     return CargoHandlingEvent(LOAD, location, voyage, completionTime)
def unload(location, voyage, completionTime):   return CargoHandlingEvent(UNLOAD, location, voyage, completionTime)
def claim(location):                            return CargoHandlingEvent(CLAIM, location)
def no_activity():                              return CargoHandlingEvent(NO_ACTIVITY) 
