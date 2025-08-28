shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))
print(another_list)

a = b = c = d = e = f = another_list # only 1 list with 8 alias or
# referencing or multiple names
print(a)

print("Adding cream")
b.append("cream")
print(c)
print(d)
