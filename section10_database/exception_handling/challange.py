import sys


def get_numbers(message:str) -> int:
    while True:
        try:
            number = int(input(message))
            return number
        except (ValueError, TypeError):
            print("Invalid input, please try again")
        except EOFError: # CMD + D
            sys.exit()
        finally: # Ideal for performing any tidying up, like closing db connection or file etc.
            print("Finally clause always executes")


x = get_numbers("Enter first number: ")
y = get_numbers("Enter second number: ")

try:
    print("{} divided by {} is {:.3f}".format(x, y, x / y))
except ZeroDivisionError:
    print("You can't divide by zero")
else:  # We can't use finally keyword , because we don't want to run this block if except clause happened
    print("Division performed successfully")