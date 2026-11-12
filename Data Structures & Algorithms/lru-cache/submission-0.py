from typing import List

class LRUCache:

    def __init__(self, capacity: int):
        self.stack: List[int] = []
        self.hashmap: dict = {}

        self.capacity: int = capacity

    def _update_stack(self, key: int) -> None:
        self.stack.remove(key)
        self.stack.append(key)

    def get(self, key: int) -> int:
        value: int = self.hashmap.get(key, -1)
        if value != -1:
            self._update_stack(key)

        return value        

    def put(self, key: int, value: int) -> None:
        # Does it already exsist
        if key in self.stack:
            self._update_stack(key)
            self.hashmap[key] = value
            return

        # If it does not
        # Check capacity, and remove one if over
        if len(self.stack) >= self.capacity:
            del self.hashmap[self.stack[0]]
            self.stack.pop(0)

        # Add new key-value pair
        self.stack.append(key)
        self.hashmap[key] = value
        return
        
