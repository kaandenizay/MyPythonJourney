menu_options = [
    "1.\tLearn Python",
    "2.\tLearn Java",
    "3.\tGo swimming",
    "4.\tHave dinner",
    "5.\tGo to bed",
    "0.\tQuit",
]

choice = "-"
while choice != "0":
    if  choice in "12345":
        print("You chose: " + menu_options[int(choice)-1])
    else:
        print("Please choose your option from the list below:")
        for option in menu_options:
            print(option)
    choice = input("\nEnter your choice: ")
