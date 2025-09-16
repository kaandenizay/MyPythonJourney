def multiply(x, y):
    result = x * y
    return result


answer = multiply(2.5, 3)
print(answer)
answer = multiply(7, 6)
print(answer)

def multiply(x: float, y: float) -> float:
    """
    Multiply 2 numbers.

    :param x: The first number to multiply.
    :param y: The number to multiply `x` by.
    :return: The product of `x` and `y`.
    """
    result = x * y
    return result


def is_palindrome(string: str) -> bool:
    """
    Check if a string is a palindrome.

    A palindrome is a string that reads the same forwards as backwards.

    :param string: The string to check.
    :return: True if `string` is a palindrome, False otherwise.
    """
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence: str) -> bool:
    """
    Check if a sentence is a palindrome.

    The function ignores whitespace, capitalisation and
    punctuation in the sentence.

    :param sentence: The sentence to check.
    :return: True if `sentence` is a palindrome, False otherwise.
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return is_palindrome(string)


def fibonacci(n: int) -> int:
    """Return the `n` th Fibonacci number, for positive `n`."""
    n_minus_2 = 0 # 2 index before n FIBONACCI_0
    n_minus_1 = 1 # 1 index before n, directly previous one FIBONACCI_1
    result = None

    if n in (0,1): # if 0 <= n <= 1
        return n

    for f in range(n - 1):
        result = n_minus_2 + n_minus_1
        n_minus_2 = n_minus_1
        n_minus_1 = result
    return result


for i in range(36):
    print(i, fibonacci(i))

word = input("Enter a word to check palindrome or not: ")
if palindrome_sentence(word):
    print("{} is a palindrome".format(word))
else:
    print("{} is not a palindrome".format(word))




def sum_eo(n, t):
    if t == 'e':
        #shorthand
        # sum(num for num in range(n) if num % 2 == 0)
        sum_numbers = sum(range(0, n, 2))
    elif t == 'o':
        sum_numbers = sum(range(1, n, 2))
    else:
        sum_numbers = -1
    return sum_numbers


print(sum_eo(10, 'e'))
print(sum_eo(7, 'o'))
print(sum_eo(11, 'spam'))
