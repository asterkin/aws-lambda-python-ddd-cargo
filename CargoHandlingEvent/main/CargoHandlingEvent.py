from nahash import dropNone

RECEIVE     = 'RECEIVE'
LOAD        = 'LOAD'
UNLOAD      = 'UNLOAD'
CLAIM       = 'CLAIM'
CUSTOMS     = 'CUSTOMS'
NO_ACTIVITY = 'NO_ACTIVITY'


def CargoHandlingEvent(eventType, location=None, voyage=None, completionTime=None):
    return dropNone({'eventType': eventType, 'location': location, 'voyage': voyage, 'completionTime': completionTime})

def load(location, voyage, completionTime):     return CargoHandlingEvent(LOAD, location, voyage, completionTime)
def unload(location, voyage, completionTime):   return CargoHandlingEvent(UNLOAD, location, voyage, completionTime)
def claim(location):                            return CargoHandlingEvent(CLAIM, location)
def no_activity():                               return CargoHandlingEvent(NO_ACTIVITY) 
