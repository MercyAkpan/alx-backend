#!bin/usr/python3
""" LFU Cache dictionary
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Defines basic caching system
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.queue = []
        self.count = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if self.queue:
                    discard = self.queue.pop(0)
                    del self.cache_data[discard]
                    print("DISCARD: {}".format(discard))
            self.queue.append(key)
            self.cache_data[key] = item
            if key in self.count:
                self.count[key] += 1
            else:
                self.count[key] = 1

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.count[key] += 1
        self.queue.remove(key)
        self.queue.append(key)
        return self.cache_data[key]
