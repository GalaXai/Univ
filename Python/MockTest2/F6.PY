import re
def f6(g,n1,n2):
    output = 0
    with open("MockTest2/people.csv","r")as file:
        x =  file.readlines()
        for i in x:
            #i = string
            gender = re.findall("Female",i)
            height= re.findall("\d{3,}",i)
            if gender == [g] and int(height[0]) >=n1 and int(height[0]) <=n2:
                output+=1
    return output
print(f6("Female",160,180))