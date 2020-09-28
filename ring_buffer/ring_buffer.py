class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.list = [None for i in range(self.capacity)]


    def append(self, item):
        self.list[self.count] = item
        if self.count <= self.capacity - 2:
            self.count += 1
        elif self.count == self.capacity - 1:
            self.count = 0

    def get(self):
        new_list = []
        for n in self.list:
            if n is not None:
                new_list.append(n)
        return new_list