import re
with open('05-Files/grades.txt.') as file:
    text = file.read()
    grades =  re.findall("\d[.]\d",text)
    sumOfGrades = 0
    for number in grades:
        sumOfGrades += float(number)
print("{:.2f}".format(sumOfGrades/len(grades)))