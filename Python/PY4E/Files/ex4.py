import re
with open("PY4E/Files/romeo.txt","r") as file:
    output = [""]
    x = file.read()
    y = re.findall("\w+",x)
    for word in y:
        flag = True
        for i in range(len(output)):
            if word == output[i]:
                flag = False
                break
            else:
                continue
        if flag == True:
            output.append(word)
    output.remove("")
    print(output)
