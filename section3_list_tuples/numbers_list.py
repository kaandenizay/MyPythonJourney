empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
print(numbers)

for number_list in numbers:
    print(number_list)

    for value in number_list:
        print(value)

print("-" * 30)
print(len(even))
print(len(odd))
print("-" * 30)
print("Mississippi".count("s"))
print("-" * 30)


even.extend(odd)
print(even)
another_even = even
print(another_even)

even.sort()
print(even)
even.sort(reverse=True)
print(even)
print(another_even)

empty_new_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
empty_new_list = even + odd
print(empty_new_list)

sorted_numbers = sorted(empty_new_list, reverse=True)
print(sorted_numbers)

digits = sorted("432985617")
print(digits)

new_list = list(empty_new_list)
print(new_list)

print(new_list is empty_new_list)
print(new_list == empty_new_list)

neww_list = empty_new_list.copy()
print(neww_list)
print(neww_list is empty_new_list)