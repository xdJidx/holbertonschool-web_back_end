#!/usr/bin/python3
""" LIFO Caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if self.queue:
                    discard = self.queue.pop()
                    del self.cache_data[discard]
                    print("DISCARD: {}".format(discard))
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)
