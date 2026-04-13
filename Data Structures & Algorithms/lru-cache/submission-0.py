class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map keys to Nodes like {1, Node5},{2,Node3}

        # Left points to LRU and Right points to Most Recently Used
        # creating dummy nodes to avoid checking for multiple error conditions
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove given node
    def remove(self, node):
        before, after = node.prev, node.next
        before.next, after.prev = after, before

    # insert at right most
    def insert(self, node):
        before, after = self.right.prev, self.right
        before.next = after.prev = node
        node.prev, node.next = before, after

    # get the value of key, make it most requently added
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            #if capacity increases, remove node from list and from cache map
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
        self.printCache()

    def printCache(self):
        for ele in self.cache:
            print(ele)