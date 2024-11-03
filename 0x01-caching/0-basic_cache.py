#!/usr/bin/env python3
""" BasicCache module implementing a simple caching system
"""

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """ BasicCache inherits from BaseCaching and implements a simple caching system.
    """

    def put(self, key, item):
        """ Assigns an item to the cache data dictionary.

        Args:
            key (str): The key for the item to be stored.
            item (Any): The value to be stored in the cache.

        If key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

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
