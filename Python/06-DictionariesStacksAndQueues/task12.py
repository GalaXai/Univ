"""
A queue is a linear data structure in which new data is added to the end of the queue,
and data is retrieved from the beginning of the queue for further processing.
Familiarize yourself in mode detail with this data structure. Explain the concept of FIFO
"""
queue = []

# add value at the queue
def push(value):
    queue.insert(-1,value)
    
# remove the first value in queue
# and return its value    
def pop():
    if not empty():
        return queue.pop()
    else:
        return None
    
# return true if the queue is empty
def empty():
    return len(queue) == 0

# display queue
def display():
    for i in queue:
        print(i, end=" ")
    print()

display()
push(3)
push(7)
push(5)
display()
pop()
display()
pop()
pop()
print(empty())