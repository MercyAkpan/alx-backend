#!/usr/bin/env python3
"""
This method contains a class BaseCache that 
inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching
class BasicCache(BaseCaching):
    """
    This class will inherit from BaseCaching
    and it is a caching system
    """
    def put(self, key, item):
        """
        This method will add an item in the cache
        """
        if (key is None) or (item is None):
            return
        self.cache_data[key] = item
        return
    
    def get(self, key):
        """
        This method will get an item by key from the cache
        """
        if (key is None) or (key not in self.cache_data):
            return None
        return self.cache_data[key]