class Dll:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = Dll(value=None, prev=None, next=None)  # default None
        self.len = 0
        self.capacity = capacity

    def _add_infront_of_the_cache(self, node: Dll):
        f_node = self.cache.next
        self.cache.next = node
        node.prev = self.cache.next
        node.next = f_node
        if f_node:
            f_node.prev = node

    def _remove_node_from_ll(self, node: Dll):
        prev = node.prev
        if prev is not None:
            prev.next = node.next
        if node.next is not None:
            node.next.prev = prev

    def get(self, key: int) -> int:
        curr = self.cache.next
        while curr is not None:
            if curr.val[0] == key:
                self._remove_node_from_ll(curr)  # remove it add it to the next
                self._add_infront_of_the_cache(curr)  # add it in front of the Cache
                return curr.val[1]
            curr = curr.next
        return -1


    def put(self, key: int, value: int) -> None:
        if self.len==self.capacity:
            pass
        else:
            node = Dll(value=value, prev=self.cache)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
