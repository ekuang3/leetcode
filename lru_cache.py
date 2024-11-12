# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

from collections import deque

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}  # key -> value
        self.order = deque()  # to maintain the access order

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            # Move the key to the end of the deque (mark as recently used)
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            # Update the value and move it to the end of the deque
            self.cache[key] = value
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache) >= self.capacity:
                # Evict the least recently used key (the first element in the deque)
                lru_key = self.order.popleft()
                del self.cache[lru_key]

            self.cache[key] = value
            self.order.append(key)

# Usage:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)

if __name__=='__main__':

    pass

    # Input:
    # ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    # [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

    # Output:
    # [null, null, null, 1, null, -1, null, -1, 3, 4]