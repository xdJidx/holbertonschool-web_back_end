#!/usr/bin/env python3
""" Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        self.cache_data[key] = item
        if key or item is None:
            return

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
