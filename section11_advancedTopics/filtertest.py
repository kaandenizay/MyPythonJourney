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

for meal in menu:
    if "spam" not in meal:
        print(meal)

print("*" * 50)

meals = [meal for meal in menu if "spam" not in meal]
print(meals)


def not_spam(meal_list: list):
    return "spam" not in meal_list


print("*" * 50)
spamless_meal = list(filter(not_spam, meals))
print(spamless_meal)