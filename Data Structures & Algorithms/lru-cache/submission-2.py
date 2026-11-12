from typing import List

class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key: int = key
        self.value: int = value
        self.left: Node | None = None
        self.right: Node | None = None
    
class LRUCache:
    def __init__(self, capacity: int):
        # Init linked list
        self.most_recent: Node = Node(0, 0)
        self.least_recent: Node = Node(0, 0)

        # Link both nodes
        self.most_recent.right = self.least_recent
        self.least_recent.left = self.most_recent

        # Assign dict for O(1) look up
        self.cache: dict[key, Node] = {}
        self.capacity = capacity

    def _remove(self, node: Node) -> None:
        """Removes node from linked list"""
        left, right = node.left, node.right
        left.right, right.left = right, left

    def _add(self, node: Node) -> None:
        right = self.most_recent.right
        self.most_recent.right = right.left = node
        node.left, node.right = self.most_recent, right

    def get(self, key: int) -> int:
        node: Node | None = self.cache.get(key, None)
        if node:
            self._remove(node)
            self._add(node)
            return node.value
        return -1
    
    def put(self, key: int, value: int) -> None:
        # Does it exsist?
        node: Node | None = self.cache.get(key, None)
        if node:
            # Update value and order
            node.value = value
            self._remove(node)
            self._add(node)
            return

        # It does not exsist
        
        # Add new to most_Recent
        right: Node = self.most_recent.right

        node = Node(key, value) # Create node
        node.left, node.right = self.most_recent, right

        self.most_recent.right = right.left = node

        # Add to cahce
        self.cache[key] = node

        # check length and remove if necessary
        if len(self.cache) > self.capacity:
            lru: Node = self.least_recent.left
            del self.cache[lru.key]
            self._remove(lru)


        
        
