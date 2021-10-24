height = int(input("Enter your height in cm: "))
mass = int(input("Enter your weight in kg :"))
bmi = mass / height / height * 10000
print("Your Bmi is equal to {:.1f}".format(bmi))
