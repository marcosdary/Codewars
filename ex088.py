from functools import reduce

def number(bus_stops):
    return reduce(lambda ac, x: ac + x, map(lambda x: x[0] - x[1], bus_stops), 0)

