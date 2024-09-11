from collections import OrderedDict 

class LRUCache:
    def __init__(self,capacity):
        self.capacity = capacity 
        self.d = OrderedDict()
    
    def get(self,key):
        if key not in self.d:
            return -1 
        self.d[key] = self.d.pop(key)
        return self.d[key]
    
    def put(self,key,value):
        if key not in self.d:
            if len(self.d) == self.capacity:
                self.d.popitem(last=False)
        else:
            self.d.pop(key)
        self.d[key] = value 
        return self.d

lru = LRUCache(2)
print(lru.put(1, 1))
print(lru.put(2, 2))
print(lru.get(1))
print(lru.put(3, 3))
print(lru.get(2))
print(lru.put(4, 4))
print(lru.get(1))
print(lru.get(3))
print(lru.get(4))