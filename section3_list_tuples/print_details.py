name = "Tim"
age = 10

print(name, age, "Python", 2020, sep=", ", end="!!!\n")
print((name, age, "Python", 2020))

values = input("Please enter three numbers, separated by commas:")
numbers = [int(num.strip()) for num in values.split(",")]

a,b,c = numbers
print(numbers)
print(a + b - c)