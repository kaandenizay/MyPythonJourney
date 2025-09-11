menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]

meals =[]
for meal in menu:
    if "spam" not in meal:
        meals.append(meal)
    else:
        meals.append("a meal was skipped")
print(meals)

meals = [meal for meal in menu if "spam" not in meal]
print(meals)

x = 12
expression = "Twelve" if x == 12 else "unknown"
print(expression)

meals_new = [meal if "spam" not in meal else "a meal was skipped" for meal in menu]
print(meals_new)


for x in range(1,31):
    fizzbuzz = "fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
    print(fizzbuzz)


fizzbuzz_list = ["fizz buzz" if x % 15 == 0
                 else "fizz" if x % 3 == 0
                 else "buzz" if x % 5 == 0 else str(x)
                 for x in range(1,31)]
print(fizzbuzz_list)
