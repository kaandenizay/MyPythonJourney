import copy

animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": "cuddly",
}


# Referencing, not shallow copy
things = animals
animals["teddy"] = "toy"
print(things["teddy"]) # prints "toy"
print(animals["teddy"])
animals["teddy"] = "cuddly" # Reverse the update

# Perform a shallow copy
things = animals.copy() # We have now 2 separate dictionaries with same reference lists

animals["teddy"] = "toy"
print(things["teddy"]) # prints "cuddly"
print(animals["teddy"])



# Perform a deep copy
things = copy.deepcopy(animals)
"""
deepcopy will also copy any objects that are contained in whatever you're
copying
"""


print(id(things["teddy"]), things["teddy"])
print(id(animals["teddy"]), animals["teddy"])
print(id(things["elephant"]), things["elephant"])
print(id(animals["elephant"]), animals["elephant"])

print()

things["elephant"].append("toy")
print(things["elephant"])
print(animals["elephant"])