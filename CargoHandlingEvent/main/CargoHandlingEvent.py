"""Encapsulates CargoHandlingEvent Repository and all relevant computations."""

import matte

RECEIVE     = 'RECEIVE'
LOAD        = 'LOAD'
UNLOAD      = 'UNLOAD'
CLAIM       = 'CLAIM'
CUSTOMS     = 'CUSTOMS'
NO_ACTIVITY = 'NO_ACTIVITY'

CARGO = 'cargo'
TIMESTAMP = 'completion_time'

Events = matte.repository('CargoHandlingEvents', hashKey = {CARGO : str}, rangeKey = {TIMESTAMP : int})

##ValueObject types for interface protection
def CargoHandlingEvent(cargo, event_type, location=None, voyage=None, completion_time=None):
    return matte.drop_nulls({CARGO: cargo, 'event_type': event_type, 'location': location, 'voyage': voyage, TIMESTAMP: completion_time})

#No need for cargo id in next activity event
def load(location, voyage, completion_time):     return CargoHandlingEvent(None, LOAD, location, voyage, completion_time)
def unload(location, voyage, completion_time):   return CargoHandlingEvent(None, UNLOAD, location, voyage, completion_time)
def claim(location):                             return CargoHandlingEvent(None, CLAIM, location)
def no_activity():                               return CargoHandlingEvent(None, NO_ACTIVITY) 
