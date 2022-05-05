import time
import datetime


class World(object):
    big_bang = time.clock()
    continents = []


# The world object should contain just info on when it was created
# and the list of continents.  this holds the instance collection of continents.
# each continent holds the collection of zones.
# each zone hold the collection of rooms
# each room holds a collection of mobs, and items
    # each mob has a collection of items, possible form
    # each item in the room, or in mobs inventory