result = True
another_result = result
print(id(result))
print(id(another_result))

result = False
print(id(result))

result = "Correct"
another_result = result
print(id(result))
print(id(another_result))

result += "ish"
print(id(result))
print(id(another_result)) # Not same anymore
print(result)
print(another_result) # Not same anymore