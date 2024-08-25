#!/usr/bin/env python3
"""
This method contains a class  LRUCache that
inherits from BaseCaching and is a LRU caching system
NT: This is a more optimised code.
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
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
        # The Ordered dict contains a dict and a doubly-linked list
        # It has more space overhead than a list, but less time complexity.
        self.linked_list = OrderedDict()

    def put(self, key, item):
        """
        This method will add an item in the cache
        """
        if (key is None) or (item is None):
            return
        # If key is to be simply updated.Move the key in the OrderedDict
        # to the end of the list.
        if (key in self.cache_data) and (key in self.linked_list):
            self.linked_list.move_to_end(key)
            self.cache_data[key] = item
            return
        if (len(self.cache_data) == BaseCaching.MAX_ITEMS):
            # Delete the first key in the OrderedDict. last=False is FIFO
            oldest_key, _ = self.linked_list.popitem(last=False)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")
        self.cache_data[key] = item
        self.linked_list[key] = None
        return

    def get(self, key):
        """
        This method will get an item by key from the cache
        """
        if (key is None) or (key not in self.cache_data):
            return None
        if (key in self.cache_data) and (key in self.linked_list):
            self.linked_list.move_to_end(key)
        return self.cache_data[key]
