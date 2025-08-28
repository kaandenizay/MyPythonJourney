
menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for meal in menu:
    if "spam" not in meal:
        print(meal)

        for item in meal:
            print(item)


for meal in menu:
    top_index = len(meal) - 1
    for index, item in enumerate(reversed(meal)):
        if item == 'spam':
            del meal[top_index - index]
    print(", ".join(meal))



for meal in menu:
    for item in meal:
        if item != 'spam':
            print(item, end=', ')

    print()

# without trailing comma, generators code
for meal in menu:
    items = ", ".join((item for item in meal if item != "spam"))
    print(items)
