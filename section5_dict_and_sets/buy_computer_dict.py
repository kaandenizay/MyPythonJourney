available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive",
                   }

current_choice = None
computer_parts = {}     # create an empty dictionary

while current_choice != "0":
    if current_choice in available_parts:
        computer_parts[current_choice] = available_parts[current_choice]
        print("Adding {}".format(available_parts[current_choice]))
    else:
        print("Please add options from the list")
        for key, value in available_parts.items():
            print(key, value, sep=": ")
        print("0: to finish")
    current_choice = input("> ")

for key, value in computer_parts.items():
    print(key, value, sep=": ")