class OwnIterable:

    def __init__(self, start : int, stop : int) -> None:
        self.current= start
        self.stop = stop
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1
    
counter = OwnIterable(1, 10)
for i in counter:
    print(i)