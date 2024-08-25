#!/usr/bin/env python3
"""
This method contains a class MRUCache that
inherits from BaseCaching and is a LRU caching system
NT: THE more optimised code is "alx-backend/0x01-caching/3-lru_cache_dict.py"
COMPLETE it.
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
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
            index = self.list.index(key)
            del self.list[index]
            del self.list[index]
            self.cache_data[key] = item
            self.list.append(key)
            self.list.append(item)
            return
        if (len(self.cache_data) == BaseCaching.MAX_ITEMS):
            list_key = self.list[len(self.list) - 2]
            del self.list[len(self.list) - 1]
            del self.list[len(self.list) - 1]
            del self.cache_data[list_key]
            print(f"DISCARD: {list_key}")
        self.cache_data[key] = item
        self.list.append(key)
        self.list.append(item)
        # print(self.list)
        return

    def get(self, key):
        """
        This method will get an item by key from the cache
        """
        if (key is None) or (key not in self.cache_data):
            return None
        if (key in self.cache_data) and (key in self.list):
            index = self.list.index(key)
            del self.list[index]
            del self.list[index]
            self.list.append(key)
            item = self.cache_data[key]
            self.list.append(item)
        return self.cache_data[key]
