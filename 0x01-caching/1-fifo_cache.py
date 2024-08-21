#!/usr/bin/env python3
"""
This method contains a class FIFOCache that
inherits from BaseCaching and is a fIFO caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    This class will inherit from BaseCaching
    and it is a FIFO caching system
    """
    def __init__(self):
        """
        This initialises the FIFO caching system
        """
        super().__init__()

    def put(self, key, item):
        """
        This method will add an item in the cache
        """
        if (key is None) or (item is None):
            return
        self.cache_data[key] = item
        if (len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS):
            first = next(iter(self.cache_data))
            self.cache_data.pop(first)
            print(f"DISCARD:",first)
        return

    def get(self, key):
        """
        This method will get an item by key from the cache
        """
        if (key is None) or (key not in self.cache_data):
            return None
        return self.cache_data[key]
