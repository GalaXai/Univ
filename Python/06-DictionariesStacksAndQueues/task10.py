#####
# Stack definition
##
stack = []
# add value at the end of the stack
def push(*args):
    for num in args:
        stack.append(num)
    
# remove the topmost element of the stack
# and return its value    
def pop():
    if not empty():
        return stack.pop()
    else:
        return None
    
# return true if the stack is empty
def empty():
    return len(stack) == 0

# display stack
def display():
    for i in stack:
        print(i, end=" ")
    print()
