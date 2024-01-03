#!/usr/bin/env python3

"""
Module: 100-lfu_cache.py
"""


from collections import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        # Dictionary to store frequency of each key
        self.frequency_dict = {}
        # Dictionary to store keys with the same frequency
        self.freq_keys_dict = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        # Update frequency and freq_keys_dict
        if key in self.cache_data:
            self.frequency_dict[key] += 1
            freq = self.frequency_dict[key]
            self.freq_keys_dict[freq].pop(key, None)
            if not self.freq_keys_dict[freq]:
                del self.freq_keys_dict[freq]

        # Check if the number of items exceeds the maximum limit
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Get the least frequently used frequency
            min_freq = min(self.freq_keys_dict.keys())
            # Get the least recently used key with the least frequency
            lru_key = self.freq_keys_dict[min_freq].popitem(last=False)[0]
            del self.cache_data[lru_key]
            del self.frequency_dict[lru_key]

            print("DISCARD: {}".format(lru_key))

        # Add the new item to the cache and update frequency and freq_keys_dict
        self.cache_data[key] = item
        self.frequency_dict[key] = 1
        self.freq_keys_dict.setdefault(1, OrderedDict())[key] = True

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        # Update frequency and freq_keys_dict
        self.frequency_dict[key] += 1
        freq = self.frequency_dict[key]
        self.freq_keys_dict[freq].pop(key, None)
        if not self.freq_keys_dict[freq]:
            del self.freq_keys_dict[freq]
        self.freq_keys_dict.setdefault(freq + 1, OrderedDict())[key] = True

        return self.cache_data[key]
