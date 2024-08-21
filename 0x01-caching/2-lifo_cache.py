#!/usr/bin/env python3
"""
This method contains a class LIFOCache that
inherits from BaseCaching and is a LIFO caching system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    This class will inherit from BaseCaching
    and it is a FIFO caching system
    """
    def __init__(self):
        """
        This initialises the FIFO caching system
        """
        # This will call the __init__ method of the parent class
        # so as to not override the parent class __init__ method
        super().__init__()
        self.list = []

    def put(self, key, item):
        """
        This method will add an item in the cache
        """
        if (key is None) or (item is None):
            return
        if (key in self.cache_data) and (key in self.list):
            # print("in here",key)
            self.list.remove(key)
            # print(self.list)
            self.list.append(key)
            self.cache_data[key] = item
            return
        if (len(self.cache_data) == BaseCaching.MAX_ITEMS):
            recent_update = self.list.pop()
            del self.cache_data[recent_update]
            print(f"DISCARD: {recent_update}")
            # last_item = self.cache_data.popitem()
            # # print(last_item[0])
            # print(f"DISCARD: {last_item[0]}")
        self.cache_data[key] = item
        self.list.append(key)
        return

    def get(self, key):
        """
        This method will get an item by key from the cache
        """
        if (key is None) or (key not in self.cache_data):
            return None
        return self.cache_data[key]
