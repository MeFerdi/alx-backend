#!/usr/bin/env python3
""" LRUCache module implementing a LRU caching system
"""

from base_caching import BaseCaching

class LRUCache(BaseCaching):
    """ LRUCache inherits from BaseCaching and implements a LRU caching system.
    """

    def __init__(self):
        """ Initialize LRUCache and call parent constructor.
        """
        super().__init__()
        self.order = []  # To keep track of the order of keys for LRU

    def put(self, key, item):
        """ Assigns an item to the cache data dictionary.

        Args:
            key (str): The key for the item to be stored.
            item (Any): The value to be stored in the cache.

        If key or item is None, this method does nothing.
        If adding this item exceeds MAX_ITEMS, discard the least recently used item.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Update existing key's value
                self.cache_data[key] = item
                # Move this key to the end of order list to mark it as recently used
                self.order.remove(key)
                self.order.append(key)
            else:
                # Add new key-value pair
                self.cache_data[key] = item
                self.order.append(key)  # Track order of keys

            # Check if we exceed max items
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Discard the least recently used (first in order)
                discarded_key = self.order.pop(0)  # Remove first key (LRU)
                del self.cache_data[discarded_key]  # Remove from cache
                print("DISCARD: {}".format(discarded_key))

    def get(self, key):
        """ Retrieves an item from the cache by key.

        Args:
            key (str): The key for the item to retrieve.

        Returns:
            The value associated with the key if it exists; None otherwise.
        """
        if key is None or key not in self.cache_data:
            return None
        
        # Update usage by moving this key to the end of order list
        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
