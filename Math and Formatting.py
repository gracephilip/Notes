# Math

# floats vs ints
print(1.2 / 2 + 1.2)

my_float = 1.2 / 2 + 1.2
print(int(my_float)) #int() chops off any remainder

my_int = 123
print(float(my_int)) #adds a decimal remainder


# VARIABLES
# Naming
snake_case = "lower case with underscore between words"
print(snake_case)

camelCase = "JavaScript uses this"
# the following is not allowed
# my variable   # spaces not allowed
# my_variable!  # no special characters
# my.variable   # no decimals
# 8 ball        # no numbers to start the variable name
# ball8         # this is allowed

#use more descriptive variable names

# Assignment
my_variable = 8
x, y = (3, 4) # assign multiple variables using a tuple (immutable list)
print(x)
print(y)


# MATH OPERATORS
# + - * /
# **n      # exponent
# //       # floor division, similar to int(), rounds down
# %        # modulo, remainder after division


# COMPOUND ASSIGNMENT OPERATORS
# +=  -=  *=  /=
x = 5
x += 1 # equivalent of x = x + 1
print(x)

x *= 3  # equivalent of x = x * 3
print(x)

x **= 0.5
print(x)


# ROUND
print(round(x, 3))


# FORMAT  "{}".format()
# for formatting TEXT
# Position:PlaceholderJustificationWidthDecorationsType

# Let's format some text
first = "Jerry"
last = "Garcia"
print(first, last)
print(first + last)

# print the first name
print("{}".format(first))

# print the last name
print("My name is {} {}.".format(first, last))  # last part is a tuple

# print    First: first     Last: last
print("First: {}\t\tLast: {}".format(first, last))


# print last, first
print("{1}, {0}".format(first, last)) # so it can be ordered how you want


# Number formatting works similarly
# You may specify d for digit/int, f for float, e for exponent to force a format
# here are some common uses


# round a float to a dedimal place   {:.3f} rounds to 3 decimal places
pi = 3.141592635897
print("{:.3}".format(pi)) # the f would make it so that its three places after the decimal

# add a sign to a number {:+}
# this works for positive and negative numbers (both use +)
print("{:+.3f}".format(pi))

# add comma formatting to number {:,}
my_number = 585209583
print("{:,}".format(my_number))

# right align  :>xd where x is the width of text
print("{:>20}".format(first))

# left align :<xd
print("{:<20} *".format(first)) # the star is so you can see the spacing

# center align :^xd
print("{:^20}".format(first))


# percent {:%} {:.2%}
print("{:.2%}".format(0.973))


# exponent  {:e} {:.2e}
print("{:.2e}".format(234323423.244))

mole = 6.02e23
print(mole / 2)

# leading zero (or other placeholder) {:.05}
print("{:+020}".format(234))

# dollars and cents?
# 142.3 >> $142.30
print("${:.2f}".format(142.3))

