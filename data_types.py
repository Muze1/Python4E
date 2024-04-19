# Data types in Python

# Literal assignment
first = "Harry"
last = "Potter"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# # Constructor function
# pizza = str("Margherita")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation
# fullname = first + " " + last
# print(fullname)
 
# fullname += "!"
# print(fullname)

# # Casting a number to a str
# decade = str(1980)
# print(type(decade))
# print(decade)

# statement = "I like Rock music from the " + decade + "s."
# print(statement)

# # Multiple lines
# multi = '''
# Hey, how are you?                                

# I was just checking in.      
#                                             All good?

# '''
# print(multi)

# # Escaping special characters
# sentence = 'I\'m back at work!\tHey!\n\nWhere\'s that at\\located?'
# print(sentence)

# # String Methods
# print(first)
# print(first.lower())
# print(first.upper())
# print(first)

# print(multi.title())
# print(multi.replace("good", "okay"))

# print(len(multi))
# multi += "                                          "
# multi = "                                         " + multi
# print(len(multi))
# print(len(multi.strip()))
# print(len(multi.lstrip()))
# print(len(multi.rstrip()))

print("")

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "£1".rjust(4))
print("Muffin".ljust(16, ".") + "£2".rjust(4))
print("Cheesecake".ljust(16, ".") + "£4".rjust(4))

print("")

# String index values
print(first[1])
print(first[-1])
print(first[1:])

# Methods returning Boolean data
print(first.startswith("H"))
print(first.endswith("F"))