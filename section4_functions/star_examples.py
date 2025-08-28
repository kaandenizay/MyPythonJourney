numbers = (0, 1, 2, 3, 4, 5)

# print(numbers, sep=";")
# print(*numbers, sep=";")
"""
When you use *(asterisk) before an object, it unpacks the any sequence type
Rather than (0, 1, 2, 3, 4, 5), print this : 0;1;2;3;4;5
Same result with below one
"""
# print(0, 1, 2, 3, 4, 5, sep=";")



"""
Instead of unpack the sequence as an argument,
We can specify that a parameter is an unpacked sequence
*args means this parameter is an unpacked tuple
So using *, we can provide a variable number of arguments to function
We can pass many arguments, even zero included
"""
def test_star(*args):
    print(args)
    for x in args:
        print(x)


test_star(0, 1, 2, 3, 4, 5)

print()
test_star()