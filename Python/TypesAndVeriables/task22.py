import random
answer = random.randrange(1, 6)
print("Guess the number 1-6")
guess = 0
attempts = 3
while guess != answer and attempts != 0:
    print("Pozostało {} próby".format(attempts))
    guess = int(input())
    attempts -= 1
if guess == answer:
    print("Congratulation the number was {}".format(answer))
else:
    print("The number was {}".format(answer))
