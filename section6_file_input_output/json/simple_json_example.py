import json

languages = [
    # ['ABC', 1987], # JSON will format as array no matter list or tuple
    ('ABC', 1987),
    ('Algol 68', 1968),
    ('APL', 1962),
    ('C', 1973),
    ('Haskell', 1990),
    ('Lisp', 1958),
    ('Modula-2', 1977),
    ('Perl', 1987),
]


"""
JSON format does not support tuples
So, the JSON created as array of arrays format
"""

DATA_PATH = '../../data/'
filename = 'test.json'
with open(DATA_PATH + filename, 'w', encoding='utf-8') as testfile:
    json.dump(languages, testfile)
    # The dump function serializes the data we give it, and write the result to the file

with open(DATA_PATH + filename, 'r', encoding='utf-8') as testfile:
    data = json.load(testfile)
print(data)
print(data[2])
