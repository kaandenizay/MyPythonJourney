LOW = 0
HIGH = 35

def factorial(n:int) -> int:
    """Return n! (0! is 1)."""
    factorial_val = 1 # (0! is 1)
    for i in range(1, n + 1):
        factorial_val *= i
    return factorial_val



for n in range(LOW, HIGH + 1):
    print("{} {}".format(n, factorial(n)))


# def factorial(n: int) -> int:
#     """
#     Return n! (0! is 1).
#
#     Valid for `n` in the range 0 to 998 (inclusive).
#     Larger values of `n` will cause a RecursionError.
#     """
#     if n <= 1:
#         return 1
#
#     return n * factorial(n - 1)
#
#
# for i in range(36):
#     print(i, factorial(i))



