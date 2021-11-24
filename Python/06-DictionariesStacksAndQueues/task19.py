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
}
#if input == number stack_number append
#if input == operators stack_operators append
#if input == "=" 
#inp = input("Type in RPN notation: ")
def reversepolishnation(inp):
    stack_numbers=[]
    stack_operators=[]
    for i in inp:
        if i ==' ':
            pass
        elif i in numbers.keys():
            stack_numbers.append(numbers[i])
        elif i in operators.keys():
            stack_operators.append(i)
        else:
            stack_operators.append(i)
    print(stack_numbers)
    print(stack_operators)

    for op in stack_operators:
        if op == "*":
            x = stack_numbers.pop(-1)
            y = stack_numbers.pop(-1)
            stack_numbers.append(x*y)
        elif op == "/":
            x = stack_numbers.pop(-1)
            y = stack_numbers.pop(-1)
            stack_numbers.append(x/y)
        elif op == "-":
            x = stack_numbers.pop(-1)
            y = stack_numbers.pop(-1)
            stack_numbers.append(x-y)
        elif op == "+":
            x = stack_numbers.pop(-1)
            y = stack_numbers.pop(-1)
            stack_numbers.append(x+y)
        elif op == "=":
            x = stack_numbers.pop(-1)
            return(x)
print(reversepolishnation("2 3 + ="))
print(reversepolishnation("2 4 1 + * ="))
print(reversepolishnation("2 3 + 4 5 + * ="))
print(reversepolishnation("8 3 1 + / 3 2 – 4 + * ="))

