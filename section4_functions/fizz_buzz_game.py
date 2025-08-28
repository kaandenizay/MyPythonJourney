LOW = 1
HIGH = 100

def fizz_buzz(number: int) -> str:
    """
    This function will return a string of fizz buzz numbers
    :param number: The number to check.
    :return: 'fizz' if the number is divisible by 3.
        'buzz' if it's divisible by 5.
        'fizz buzz' if it's divisible by both 3 and 5.
        The number, as a string, otherwise.
    """
    if number % 15 == 0:
        return 'fizz buzz'
    elif number % 3 == 0:
        return 'fizz'
    elif number % 5 == 0:
        return 'buzz'
    else:
        return str(number)


for number in range(LOW, HIGH+1):
    if number % 2 == 1:
        print("{} is {}".format(number, fizz_buzz(number)))
    else:
        user_guess = input("Your go, {} is: ".format(number))
        if user_guess.casefold() == fizz_buzz(number):
            print("Yes, correct!")
        else:
            print("Wrong answer, the correct answer was {}".format(fizz_buzz(number)))
            break
else:
    print("Congratulations, Thank you for playing!")


