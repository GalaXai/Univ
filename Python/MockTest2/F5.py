from os import makedirs


def f5(c):
    output = 0
    with open("MockTest2/poem.txt","r") as file:
        x= file.readlines()
        for i in x:
            for z in i:
                if z.lower() == c:
                    output +=1
                    break
    return output
print(f5("m"))