from tkinter.scrolledtext import example

from data import basic_plants_list, plants_list

print(plants_list[0])
print(basic_plants_list[0])

for plant in basic_plants_list:
    print(plant[0])

print("*" * 28)

for plant in plants_list:
    print(plant.name, plant[1]) # We can use both dot notation or index

print("*" * 28)

example = plants_list[0]
print(example)
example = example._replace(lifecycle="Annual")
print(example)
print("*" * 28)

for plant in plants_list:
    print(plant) # We can use both dot notation or index