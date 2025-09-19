import sys


def my_range(n: int):
    print("my_range starts")
    start = 0
    while start < n:
        print("my_range is returning {}".format(start))
        yield start # Rather than using return statement like return start
                    # yield both return and tracks the its variables
        start += 1


big_range = my_range(5) # big_range is executed but my_range not
# _ = input("line 15")
print(next(big_range)) # next func consumes first value in iterator, so list starts at "1"
print("big_range is {} bytes".format(sys.getsizeof(big_range)))

# create a list containing all the values in big_range
big_list = []

# _ = input("line 22")
for val in big_range:
    # _ = input("line 24 - inside loop")
    big_list.append(val)

print("big_list is {} bytes".format(sys.getsizeof(big_list)))
print(big_range)
print(big_list)

for i in my_range(5):
    print("i is {}".format(i))