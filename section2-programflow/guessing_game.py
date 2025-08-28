import random

highest = 10000
answer = random.randint(1, highest)
trial = 0
# print(answer) # TODO: remove after testing

print("Please guess number between 1 and {}: ".format(highest))

while True:
    guess = int(input())
    trial += 1
    if guess == answer:
        print("Correct! You guessed the number!")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")

print("You found at {} trials!".format(trial))