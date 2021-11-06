class MyHashSet:

    def __init__(self):
        self.set = []
        self.hashValue = 10
        def hash(key):
            hash = key % self.hashValue
            return hash



    def add(self, key: int) -> None:
        if (hash(key)) not in self.set:
            self.set.append(hash(key))
        

    def remove(self, key: int) -> None:
        if (hash(key)) in self.set:
            self.set.remove(hash(key))
        

    def contains(self, key: int) -> bool:
        if (hash(key)) in self.set:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

myHashSet = MyHashSet()
myHashSet.add(1)      # set = [1]
myHashSet.add(2)      # set = [1, 2]
myHashSet.contains(1) # return True
myHashSet.contains(3) # return False, (not found)
myHashSet.add(2)      # set = [1, 2]
myHashSet.contains(2) # return True
myHashSet.remove(2)   # set = [1]
myHashSet.contains(2)  # return False, (already removed)