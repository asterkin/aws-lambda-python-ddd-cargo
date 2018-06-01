"""Check whether Cargo Specification is satisfied by Itinerary."""

def is_cargo_specification_satisfied(specification, itinerary):
    if not specification: return False
    elif not itinerary or len(itinerary) == 0: return False
    start = itinerary[0]
    finish = itinerary[-1]

    return specification.origin == start.load.location and specification.destination == finish.unload.location and specification.arrival_dead_line >= finish.unload.time

