#!/usr/bin/env python3

"""
Module: 0-fifo_cache.py
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
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

        # Check if the no. of items exceed the max limit
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:

            # FIFO eveiction: remove first item added to cache
            discarded = next(iter(self.cache_data))
            del self.cache_data[discarded]
            print(f"DISCARD: {discarded}")

        # Add new item to cache
        self.cache_data[key] = item

    def get(self, key):
        """
        Gets cached items
        """
        if key is not None:
            return self.cache_data.get(key)
