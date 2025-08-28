import random

lowest = 1
highest = 10
answer = int(input("Please guess number between {0} and {1}: ".format(lowest, highest)))
trial = 0

while True:
    guess = lowest + (highest - lowest) // 2
    print("Guess: {}".format(guess))
    trial += 1
    if guess == answer:
        print("I gotta number!")
        break
    else:
        if guess < answer:
            lowest = guess + 1
        else:
            highest = guess - 1
        print("Let me try again!")
        if lowest == highest:
            print("Aha, the number should be {}!".format(lowest))
            trial += 1
            break

print("I found at {} trials!".format(trial))