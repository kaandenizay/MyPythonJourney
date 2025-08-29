choice = "-"  # initialise choice to something invalid
while choice != "0":
    # if choice in set("12345"): # We used set func here
    """
    Here set function receives an iterable object, "12345" string in 
    this example, but it takes any iterable object even list and range also
    """
    if choice in {"1", "2", "3", "4", "5"}: # We used set literal
        print("You chose {}".format(choice))
    else:
        print("Please choose your option from the list below:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo swimming")
        print("4:\tHave dinner")
        print("5:\tGo to bed")
        print("0:\tExit")

    choice = input()
