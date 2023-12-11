class OwnIterable:

    def __init__(self, data) -> None:
        self.data = data
    
    def __iter__(self):
        self.i = 0
        return self
    
    def __next__(self):
        if self.i < len(self.data):
            self.i += 1
            result = self.data[self.i - 1]
            return result
        else:
            raise StopIteration

    def __getitem__(self, key):
        return self.data[key]
    
counter = OwnIterable([1, 2, 3, 4, 5])
for i in counter:
    print(i)
print(counter[0])