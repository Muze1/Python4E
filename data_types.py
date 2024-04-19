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
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a str
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like Rock music from the " + decade + "s."
print(statement)

# Multiple lines
multi = '''
Hey, how are you?                                

I was just checking in.      
                                            All good?

'''
print(multi)