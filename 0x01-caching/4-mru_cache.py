#!/usr/bin/env python3
""" MRUCache module implementing an MRU caching system
"""

from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """ MRUCache inherits from BaseCaching and implements an MRU caching system.
    """

    def __init__(self):
        """ Initialize MRUCache and call parent constructor.
        """
        super().__init__()
        self.order = []  # To keep track of the order of keys for MRU

    def put(self, key, item):
        """ Assigns an item to the cache data dictionary.

        Args:
            key (str): The key for the item to be stored.
            item (Any): The value to be stored in the cache.

        If key or item is None, this method does nothing.
        If adding this item exceeds MAX_ITEMS, discard the most recently used item.
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
                # Discard the most recently used (last in order)
                discarded_key = self.order.pop()  # Remove last key (MRU)
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
