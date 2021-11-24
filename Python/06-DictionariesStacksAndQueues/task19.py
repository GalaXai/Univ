numbers = {
    "0":0,
    "1":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
}
operators = {
    "*": '*',
    "/": '/',
    "+": '+',
    "-": '-',
    "=": '=',
}
#if input == number stack_number append
#if input == operators stack_operators append
#if input == "=" 
#inp = input("Type in RPN notation: ")
def reversepolishnation(inp):
    stack = []
    for i in inp:
        if i ==' ':
            pass
        else:
            stack.append(i)


    print(stack)
    i=-1
    while True:
        i+=1
        if stack[i] in operators:
            if stack[i] == "*":
                y = int(stack[i-1])
                x = int(stack[i-2])
                stack.pop(i-2)
                stack.pop(i-2)
                stack.pop(i-2)
                stack.insert(i-2 , x*y)
                i-=2
            elif stack[i] == "/":
                y = int(stack[i-1])
                x = int(stack[i-2])
                stack.pop(i-2)
                stack.pop(i-2)
                stack.pop(i-2)
                stack.insert(i-2 , x/y)
                i-=2
            elif stack[i] == "-":
                y = int(stack[i-1])
                x = int(stack[i-2])
                stack.pop(i-2)
                stack.pop(i-2)
                stack.pop(i-2)
                stack.insert(i-2 , x-y)
                i-=2
            elif stack[i] == "+":
                y = int(stack[i-1])
                x = int(stack[i-2])
                stack.pop(i-2)
                stack.pop(i-2)
                stack.pop(i-2)
                stack.insert(i-2 , x+y)
                i-=2
            elif stack[i] == "=":
                x = stack[i-1]
                return(x)


    #for op in stack_operators:
    #    if op == "*":
    #        x = stack_numbers.pop(-1)
    #        y = stack_numbers.pop(-1)
    #        stack_numbers.insert(0,x*y)
    #    elif op == "/":
    #        x = stack_numbers.pop(-1)
    #        y = stack_numbers.pop(-1)
    #        stack_numbers.insert(0,x/y)
    #    elif op == "-":
    #        x = stack_numbers.pop(-1)
    #        y = stack_numbers.pop(-1)
    #        stack_numbers.insert(0,x-y)
    #    elif op == "+":
    #        x = stack_numbers.pop(-1)
    #        y = stack_numbers.pop(-1)
    #        stack_numbers.insert(0,x+y)
    #    elif op == "=":
    #        x = stack_numbers.pop(-1)
    #        return(x)
print(reversepolishnation("2 3 + ="))
print(reversepolishnation("2 4 1 + * ="))
print(reversepolishnation("2 3 + 4 5 + * ="))
print(reversepolishnation("8 3 1 + / 3 2 - 4 + * ="))

