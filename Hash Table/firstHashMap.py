class MyHashMap:

    def __init__(self):
        self.map = []   

    def get(self, key: int) -> int:
        for value in self.map:
            if key == value[0]:
                return 1
        return -1

    def remove(self, key: int) -> None:
        pass

    def put(self, key: int, value: int) -> None:
        if self.get(key) == 1:
            print("Replace")
        else:
            self.map.append([key, value])
            print(self.map)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

myHashMap = MyHashMap()
myHashMap.put(1, 1) # The map is now [[1,1]]
myHashMap.put(2, 2) # The map is now [[1,1], [2,2]]
myHashMap.get(1)    # return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3)    # return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1) # The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2)    # return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2) # remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2)    # return -1 (i.e., not found), The map is now [[1,1]]