# trial_1 = {"Bob", "Charley", "Georgia", "John"}
# trial_2 = {"Anne", "Charley", "Eddie", "Georgia"}
#
# check_set = trial_1.intersection(trial_2)
# print(check_set)

farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}
potential_rides = {"donkey", "horse", "camel"}

intersection = farm_animals & wild_animals & potential_rides
print(intersection)

mounts = farm_animals.intersection(wild_animals, potential_rides)
print(mounts)



text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

text_list = text.split()
preps_used = prepositions.intersection(text_list)
print(preps_used)