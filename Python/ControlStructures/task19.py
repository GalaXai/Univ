years = int(input("Enter the dog's age in human years: "))
dogs_years = 0
if years >= 2:
    dogs_years = 21
    years -= 2
elif years == 1:
    dogs_years = 10.5
    years -= 1
dogs_years += years*4
print("The dog's age in dog’s years is {} years.".format(dogs_years))
