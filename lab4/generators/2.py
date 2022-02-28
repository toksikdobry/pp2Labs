class EvenNumbers:
    def __init__(self, end):
        self.end = end
    
    def __iter__(self):
        self.a = 0
        return self
        
    def __next__(self):
        if self.a <= self.end:
            i = self.a
            self.a += 2
            return i
        else:
            raise StopIteration

b = EvenNumbers(100)
iter = iter(b)

for i in iter:
    print(i, end = ", ")
    
