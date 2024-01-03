#!/usr/bin/env python3

"""
Module: 3-lru_cache.py
"""


from collections import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    Implements LRU caching
    """

    def __init__(self):
        """
        Initializes LRU
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
            discarded, _ = self.order_dict.popitem(last=False)
            del self.cache_data[discarded]
            print(f"DISCARD: {discarded}")

        # Add new item and update te dict
        self.cache_data[key] = item
        self.order_dict[key] = True

    def get(self, key):
        """
        Retrieves  cached item
        """
        if key is not None:
            return self.cache_data.get(key)
