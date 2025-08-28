number = input("Please enter a series of numbers, using any separators you prefer: ")
# seperators = number[1::4]
separators = ""

for char in number:
    if not char.isnumeric():
        separators += char

print(separators)


values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
capitalLetters = ""

for char in quote:
    if char.isupper():
    # if char == char.upper() and char.isalpha():
        capitalLetters += char

print(capitalLetters)