def BMI_calc(height,mass):
    return mass / height / height * 10000
mass = int(input("Enter your mass in kg : "))
height = int(input("Enter your height in cm : "))
print(" your BMI is equal to {}".format(BMI_calc(height,mass)))

BMI =  lambda height,mass: mass / height / height * 10000
print(BMI(182,81))