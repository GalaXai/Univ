import random
def read_number():
    guess = int(input("Enter your number: "))
    return guess
def generate_number():
    answer = random.randrange(1,9)
    return answer
guess = 0
answer = generate_number()
attempts = 3
while guess!=answer and attempts > 0:
    guess = read_number()
    attempts -=1
if guess == answer :
    print("congratulation")
else:
    print(" The number was equal to {}".format(answer))
