
# jabber = open("../Jabberwocky.txt", "r")
"""
open function returns an object that we can use to get data from file
"""

# for line in jabber:
#     # print(line, end="") # Same result
#     print(line.strip())
#     print(line.rstrip()) # right strip, look last line
#     print(line.lstrip()) # left strip
# jabber.close()

with open('../data/Jabberwocky.txt', "r") as jabber:
    for line in jabber:
        print(line.rstrip())

"""
This is preferred, because the file is automatically closed when the
with block terminates
"""

with open('../data/Jabberwocky.txt', "r") as jabber:
    lines = jabber.readlines()
print(lines)
print(lines[-1:])
"""
readlines method returns a list, containing strings for each line
"""

for line in reversed(lines):
    print(line, end="")
print("*" * 50 + "\n")

with open('../data/Jabberwocky.txt') as jabber: # Default mode is reading 'r'
    text = jabber.read()
    print(text)
"""
read method doesnt split the lines up. Instead, 
it returns a single string containing all the characters in file
"""


with open('../data/Jabberwocky.txt') as jabber:
    while True:
        line = jabber.readline().rstrip()
        print(line)
        if 'jubjub' in line.casefold():
            break

print('*' * 80)

with open('../data/Jabberwocky.txt') as jabber:
    for line in jabber:
        print(line.rstrip())
        if 'jubjub' in line.casefold():
            break