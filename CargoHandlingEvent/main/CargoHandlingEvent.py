"""Encapsulates CargoHandlingEvent Repository and all relevant computations."""
from mattea import dropNone, Repository

RECEIVE     = 'RECEIVE'
LOAD        = 'LOAD'
UNLOAD      = 'UNLOAD'
CLAIM       = 'CLAIM'
CUSTOMS     = 'CUSTOMS'
NO_ACTIVITY = 'NO_ACTIVITY'

CARGO = 'cargo'
TIMESTAMP = 'completionTime'

Events = Repository('CargoHandlingEvents', hashKey = {CARGO : str}, rangeKey = {TIMESTAMP : int})

def CargoHandlingEvent(cargo, eventType, location=None, voyage=None, completionTime=None):
    return dropNone({CARGO: cargo, 'eventType': eventType, 'location': location, 'voyage': voyage, TIMESTAMP: completionTime})

#No need for cargo id in next activity event
def load(location, voyage, completionTime):     return CargoHandlingEvent(None, LOAD, location, voyage, completionTime)
def unload(location, voyage, completionTime):   return CargoHandlingEvent(None, UNLOAD, location, voyage, completionTime)
def claim(location):                            return CargoHandlingEvent(None, CLAIM, location)
def no_activity():                              return CargoHandlingEvent(None, NO_ACTIVITY) 
