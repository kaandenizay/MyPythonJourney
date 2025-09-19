text = "what have the romans ever done for us"

capitals = [char.upper() for char in text]
print(capitals)

words = [word.upper() for word in text.split(' ')]
print(words)

lc_words = text.split(' ') # no necessary to use comprehension, because we are not doing operation for elements over iteration
print(lc_words)