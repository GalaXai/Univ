numbers = [15,8,31,47,2,19]
wynik = 0
for x in range(len(numbers)):
    wynik += numbers[x]

print(wynik/len(numbers))
#OR
print(sum(numbers)/len(numbers))