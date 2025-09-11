import sys

big_range = range(10000)
# big-range is a special case of iterator, called a generator

print("big range is {} bytes".format(sys.getsizeof(big_range)))


# create a list containing all the values in big range
big_list = []
for val in big_range:
    big_list.append(val)

print("big list is {} bytes".format(sys.getsizeof(big_list)))

big_list2 = list(big_list)
print("big list2 is {} bytes".format(sys.getsizeof(big_list2)))