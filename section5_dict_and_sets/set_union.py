farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}

all_animals_1 = farm_animals.union(wild_animals)
all_animals_2 = wild_animals.union(farm_animals)
print(all_animals_1)
print(all_animals_2) # exactly same

all_animals_3 = wild_animals | farm_animals
print(all_animals_3)

from prescription_data import adverse_interactions

meds_to_watch = set()

# for interaction in adverse_interactions:
#     # meds_to_watch = meds_to_watch.union(interaction)
#     # meds_to_watch = meds_to_watch | interaction
#         """
#         union method and operator creates new set each time
#         Instead, update method, modifies the original set
#         """
#     # meds_to_watch.update(interaction)
#     meds_to_watch |= interaction  # same with above, operator form

meds_to_watch.update(*adverse_interactions)
"""
update methods also receives an iterable, (a number of iterable),
so we can use it also unpacking sequence arguments
The above methods do same result without using for loop and it's
more Pythonic way
"""

print(sorted(meds_to_watch))
print(*sorted(meds_to_watch), sep='\n')
