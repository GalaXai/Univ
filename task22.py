import random
answer = random.randrange(1,6)
guess = 0
attempt = 3
while guess != answer and attempt != 0:
    print("Guess the number 1-6")
    #print(answer)
    guess = int(input())
    #print(guess)
    attempt -= 1
if guess == answer:
    print("Congratulations the number was {}".format(answer))
else:
    print("The number was {}".format(answer))