# There are two type of errors; syntax errors or exceptions

# x = 8 = 5 # Syntax error, can be correcting by typing correct one, fixing code
# x = 8 - 5
# y = x / 0 # Exception - ZeroDivisionError

def factorial(n):
    if n < 0:
        print(n / 0)
        return n
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def error_catcher(n:int):
    try:
        print(factorial(n))
    except (RecursionError, OverflowError) as rec_error:
        print(rec_error)
    except ZeroDivisionError as division_error:
        print(division_error)


print(factorial(5))
print(factorial(50))
print(factorial(500))

error_catcher(1000)
error_catcher(-5)

print("Program terminated.")