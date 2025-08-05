

# Basic list
my_list = [1, 2, 3, 4]

# Nested list
nested_list = [1, [2, 3], [4, 5]]

# Length
print("Length of my_list:", len(my_list))

# Concatenation
list2 = [5, 6]
concat = my_list + list2
print("Concatenated list:", concat)

# Membership
print("Is 3 in my_list?", 3 in my_list)
print("Is 10 in my_list?", 10 in my_list)

# Iteration
print("Iterating through my_list:")
for item in my_list:
    print(item, end=" ")
print()

# Indexing
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# Slicing
print("Slice [1:3]:", my_list[1:3])
print("Slice from start to 2:", my_list[:2])
print("Slice from 2 to end:", my_list[2:])
print("Full slice:", my_list[:])

# Nested list access
print("Accessing nested element:", nested_list[1][0])  # Should print 2
