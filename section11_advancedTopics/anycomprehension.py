from data import people, plants_list, plants_dict

if all([person[1] for person in people]):
    # Using all is much simpler than iterating over the list
    # checking email address
    print("Sending email")
else:
    print("User must edit the list of recipients")


if any([plant.plant_type == 'Grass' for plant in plants_list]):
    print("This pack contains grass plants")
else:
    print("No grasses in this pack")


if any(plant.plant_type == 'Grass' for plant in plants_dict.values()):
    print("This dict contains grasses")
else:
    print("No grasses in this dict")


if any(plants_dict[key].plant_type == 'Grass' for key in plants_dict):
    print("This dict contains grasses")
else:
    print("No grasses in this dict")