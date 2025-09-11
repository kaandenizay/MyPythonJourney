def centre_text(*args):
    # text = ""
    # for arg in args:
    #     text += str(arg) + "-"
    text = "-".join([str(arg) for arg in args]) # it's list comprehension
    # text = "-".join(str(arg) for arg in args) # without brackets it's generator
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


centre_text("spam and eggs")
centre_text("spam, spam and eggs")
centre_text(123)
centre_text("first", "second", 3 ,4, "spam")
