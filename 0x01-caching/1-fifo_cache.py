#!/usr/bin/env python3
""" FIFOCache module implementing a FIFO caching system
"""

from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """ FIFOCache inherits from BaseCaching and implements a FIFO caching system.
    """

    def __init__(self):
        """ Initialize FIFOCache and call parent constructor
        """
        super().__init__()
        self.order = []  # To keep track of the order of keys

    def put(self, key, item):
        """ Assigns an item to the cache data dictionary.

        Args:
            key (str): The key for the item to be stored.
            item (Any): The value to be stored in the cache.

        If key or item is None, this method does nothing.
        If adding this item exceeds MAX_ITEMS, discard the first item added.
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                self.order.append(key)  # Track order of keys
            self.cache_data[key] = item
            
            # Check if we exceed max items
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Discard the first item (FIFO)
                discarded_key = self.order.pop(0)  # Remove first key
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
        return self.cache_data[key]
