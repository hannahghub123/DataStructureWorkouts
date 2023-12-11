class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None]* size

    def hashfunction(self, key):
        return sum(ord(char) for char in key) % (self.size)
    
    def insert(self, key, value):
        index = self.hashfunction(key)

        if self.table[index] is None:
            self.table[index] = []

        self.table[index].append((key, value))

    def get(self, key):
        index = self.hashfunction(key)

        if self.table[index] is not None:
            for k,v in self.table[index]:
                if k == key:
                    return v
                
        raise KeyError("Element not found")
    
    def remove(self, key):
        index = self.hashfunction(key)

        if self.table[index] is not None:
            for i,(k,v) in enumerate(self.table[index]):
                if k==key:
                    del self.table[index][i]
                    return
                
        raise KeyError("Element not found")
    


h = HashTable(10)

h.insert("name","hannah")
h.insert("age",22)
h.insert("place","pta")

print(h.get("name"))
print(h.get("age"))

h.remove("place")