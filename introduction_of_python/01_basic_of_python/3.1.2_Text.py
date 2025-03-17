# python can manuplate text (represented as string) as well.
# python string written in single quotes ('...') or double quotes ("...") with the same result. and '''...''' can be used to write multi-line strings.

first_string = 'Hello'
second_string = "World"
print(first_string)
print(second_string)

# strings can be concatenated using + operator.
print(first_string + second_string)

multiple_line_string = '''This is a 
multi-line string'''
print(multiple_line_string)

# \n is used to escape the newline character.
print("first line \nsecond line")

# if you don't want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote:
print(r"C:\some\name")

# u can do slicing of strings.
word = 'Python'
print(word[0])
print(word[-1])
print(word[1:3])
print(word[3:])