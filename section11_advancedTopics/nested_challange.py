
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i, i * j)

for result in [(i, i * j) for i in range(1,11) for j in range(1,11)]:
    print(result)

print("*" * 50)
for result in [[(i, i * j) for j in range(1, 11)] for i in range(1, 11)]:
    print(result)

print("*" * 50)
for x, y in ((i, i * j) for i in range(1,11) for j in range(1,11)): # this is generation not list comprehension
                                # and much more efficient than list comprehension if
    print(x, y)