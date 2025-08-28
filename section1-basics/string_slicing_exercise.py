parrot = "Norwegian Blue"

print(parrot[0:6])  # Norweg
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])

print(parrot[10:14])
print(parrot[10:])

print(parrot[:6])
print(parrot[6:])

print(parrot[:6] + parrot[6:])

print(parrot[:])

print(parrot[0:6])  # Norweg
print(parrot[-14:-8])

print(parrot[-4:-2])    # Bl
print(parrot[-4:12])    # Bl


# Slicing with steps
print(parrot[0:6:2])    # Nre
print(parrot[0:6:3])    # Nw

number = "9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])

# Slicing back
letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[::-1]
print(backwards)

print(letters[16:13:-1])
print(letters[4::-1])
print(letters[:-9:-1])

print(letters[-4:])
print(letters[-1:])
print(letters[:1])
print(letters[0])






