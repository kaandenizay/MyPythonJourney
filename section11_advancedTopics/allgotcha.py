entries2 = [1, 2, 3, 4, 5]

print("all: {}".format(all(entries2))) # all the item in the list of true values
print("any: {}".format(any(entries2))) #at least one of the item in list is true

entries = []

if entries:
    print("all: {}".format(all(entries)))
else:
    print(False)
print("any: {}".format(any(entries)))

result = bool(entries) and all(entries)
print(result)
