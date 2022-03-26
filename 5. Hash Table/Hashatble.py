class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None

t = HashTable()
t['March 1'] = 12
t['March 2'] = 13
t['March 3'] = 11

print(t['March 2'])
print(t.arr)

t['March 2'] = 15
print(t['March 2'])
print(t.arr)

del t['March 3']
print(t['march 3'])
print(t.arr)