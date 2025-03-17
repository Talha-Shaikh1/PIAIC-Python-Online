# Python knows a number of compound data types, used to group together other values. The most versatile is the list, which can be written as a list of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type.

my_list = [1, 2, 3, 4, 5]
print(my_list)

# Like string (and all other built-in sequence types), lists can be indexed and sliced:
print(my_list[0])
print(my_list[2:4])

# All slice operations return a new list containing the requested elements. This means that the following slice returns a new (shallow) copy of the list:
print(my_list[:])

# Lists also support operations like concatenation:
print(my_list + [6, 7, 8, 9])

# Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:
my_list[0] = 0
print(my_list)

# You can also add new items at the end of the list, by using the append() method (we will see more about methods later):
my_list.append(6)

# You can find the length of a list using the len() function:
print(len(my_list))

# You can nest lists, which means to create lists that contain other lists. For example:
nested_list = [my_list, [10, 11, 12]]
print(nested_list)
print(nested_list[0][1])

# As we will see later, there are also other data types that can be used to build lists. For example, the array.array() type described at the end of this section can be used to represent lists of numbers and is more efficient than lists for this purpose.

# To access the last element of a list, you can use negative indexing:
print(my_list[-1])

# You can also use negative indexing to access elements from the end of the list:
print(my_list[-2])

