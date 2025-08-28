name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

if age >= 18:
    print("You are old enough to vote")
    print("Please put an X in the box")
else:
    print("Please come back in {0} years".format(18 - age))


tree1 = 'cinar'
tree2 = 'mese'

if tree1 == tree2:
    print("The trees are the same")
else:
    print("The trees are different.")

x = 5
y = 7

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is smaller than y")
else:
    print("x equals y")