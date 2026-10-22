class MyHashMap:

    def __init__(self):
        self.hashmap: List[(int, int)] = []
        
    def _get_index(self, key: int) -> int | None:
        for i, (cur_key, _) in enumerate(self.hashmap):
            if cur_key == key:
                return i

        return None

    def put(self, key: int, value: int) -> None:
        i = self._get_index(key)

        if i is not None:
            self.hashmap.pop(i)
            self.hashmap.append((key, value))
        else:
            self.hashmap.append((key, value))

    def get(self, key: int) -> int:
        i = self._get_index(key)

        if i is not None:
            return self.hashmap[i][1]

        return -1

    def remove(self, key: int) -> None:
        i = self._get_index(key)
        if i is not None:
            self.hashmap.pop(i)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)