print(__file__) # prints full name of the python file

numbers = [1,2,3,4,5,6,7,8,9,10]

squares = [number ** 2 for number in numbers] # comprehension the part after equal sign
# squares = [number ** 2 for number in range (1, 7)] # it accepts any type of iteration in second part

print(squares)