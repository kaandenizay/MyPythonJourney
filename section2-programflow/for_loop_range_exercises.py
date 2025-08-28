for i in range(0,10):
    print("i is now {}".format(i))
print("-" * 50)

for i in range(10):
    print("i is now {}".format(i))
print("-" * 50)

for i in range(0,20,2):
    print("i is now {}".format(i))
print("-" * 50)

for i in range(10,-5,-2):
    print("i is now {}".format(i))

for i in range(0,11):
    for j in range(0,10):
        print("{0} times {1} is {2} ".format(i,j,i*j))
    print("-" * 20)


for i in range(21):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)