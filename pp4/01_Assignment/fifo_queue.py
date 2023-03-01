class FIFO_queue:
    def __init__(self) -> None:
        self.queue = []

    def add(self,a):
        self.queue.append(a)

    def pop(self):
        return self.queue.pop(0)
    
q = FIFO_queue()
q.add(5)
q.add(3)
print(q.pop())