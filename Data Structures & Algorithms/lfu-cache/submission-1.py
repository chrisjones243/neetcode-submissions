class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key: int = key
        self.value: int = value
        self.freq: int = 1
        self.prev: Node | None = None
        self.next: Node | None = None

class LRULinkedList:
    def __init__(self):
        self.MRU, self.LRU = Node(0, 0), Node(0, 0)

        self.MRU.prev = self.LRU
        self.LRU.next = self.MRU

    def add(self, node) -> None:
        prev: Node = self.MRU.prev
        self.MRU.prev = node
        prev.next = node
        node.next, node.prev = self.MRU, prev

    def remove(self, node) -> None:
        prev, nxt = node.prev, node.next
        nxt.prev, prev.next = prev, nxt
        node.prev = node.next = None

    def get_LRU(self) -> Node:
        return self.LRU.next

    def is_empty(self) -> bool:
        if self.MRU.prev == self.LRU and self.LRU.next == self.MRU:
            return True
        return False

class LFUCache:

    def __init__(self, capacity: int):
        self.freq_map: dict[int, LRULinkedList] = {}
        self.cache: dict[int, Node] = {}

        self.capacity: int = capacity
        self.count: int = 0

        self.min_freq = 0

    def _add(self, node: Node) -> None:
        linked_list = self.freq_map.get(node.freq, LRULinkedList())
        linked_list.add(node)
        self.freq_map[node.freq] = linked_list
        self.cache[node.key] = node

    def _remove(self, node: Node) -> None:
        self.freq_map[node.freq].remove(node)
        
        # Need to check if linked list is empty, 
        # if so remove from freq_map
        if self.freq_map[node.freq].is_empty():
            del self.freq_map[node.freq]
            if node.freq == self.min_freq:
                self.min_freq += 1

    def _evict(self, node: Node) -> None:
        self._remove(node)
        del self.cache[node.key]
        self.count -= 1

    def get(self, key: int) -> int:
        node: Node | None = self.cache.get(key, None)
        if node:
            self._remove(node)
            node.freq += 1
            self._add(node)
            return node.value

        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        node: Node | None = self.cache.get(key, None)

        if node:
            self._remove(node)
            node.freq += 1
            node.value = value
            self._add(node)
            
            return

        # Remove LFU when above capacity
        if self.count == self.capacity:
            lru: Node = self.freq_map[self.min_freq].get_LRU()
            self._evict(lru)

        # A new node will have to be created and added
        node = Node(key, value)
        self._add(node)
        self.count += 1
        self.min_freq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)