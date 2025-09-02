my_tuple = (10, "Python", 3.14, "Code", 5, "Immutable")
print("Third element:", my_tuple[2])
print("Fifth element:", my_tuple[4])

sliced_tuple = my_tuple[1:5]
print("Sliced tuple:", sliced_tuple)

count_code = my_tuple.count("Code")
print("Count of 'Code':", count_code)

a, b, c, d, e, f = my_tuple
print(a, b, c, d, e, f)

new_tuple = my_tuple + ("New", "Tuple")
print("Concatenated tuple:", new_tuple)