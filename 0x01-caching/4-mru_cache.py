#!/usr/bin/env python3

"""
Module: 4-mru_cache.py
"""


from collections import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    Implements MRU caching
    """

    def __init__(self):
        """
        Initializes MRU
        """
        super().__init__()
        self.order_dict = OrderedDict()

    def put(self, key, item):
        """
        Adds an item to cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Get the last recently used key and del it
            discarded, _ = self.order_dict.popitem(last=True)
            del self.cache_data[discarded]
            print(f"DISCARD: {discarded}")

        # Add new item and update te dict
        self.cache_data[key] = item
        self.order_dict[key] = False

    def get(self, key):
        """
        Retrieves  cached item
        """
        if key is None or key not in self.cache_data:
            return None

        # Move accessed key to the end of the order_dict (most recently used)
        self.order_dict.pop(key, None)
        self.order_dict[key] = True

        return self.cache_data[key]
