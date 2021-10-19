print("Enter your height in cm:")
height = int(input())
print("Enter your weight in kg:")
mass = int(input())
bmi = mass / height / height * 10000
print("Your Bmi is equal to {:.1f}".format(bmi))
