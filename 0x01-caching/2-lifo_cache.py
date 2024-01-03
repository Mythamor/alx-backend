#!/usr/bin/env python3

"""
Module: 0-lifo_cache.py
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    Implements FIFO caching
    """

    def __init__(self):
        """
        Initializes FIFO
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds an item to cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Get the last key and del it
            discarded = list(self.cache_data.keys())[-1]
            del self.cache_data[discarded]
            print(f"DISCARD: {discarded}")

        # Add new item
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves  cached item
        """
        if key is not None:
            return self.cache_data.get(key)
