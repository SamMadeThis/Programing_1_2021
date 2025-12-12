# 3.1.2. Strings

# They can be enclosed in single quotes ('...')
# or double quotes ("...") with the same result.
# \ can be used to escape quotes

print ('spam eggs')  # single quotes
print ('doesn\'t')  # use \' to escape the single quote...
print ("doesn't")  # ...or use double quotes instead
print ('"Yes," they said.')
print ("\"Yes,\" they said.")
print ('"Isn\'t," they said.')

# the output string is enclosed in quotes 
# special characters are escaped with backslashes

print('"Isn\'t," they said.')

s = 'First line.\nSecond line.'  # \n means newline
s  # without print(), \n is included in the output

print(s)  # with print(), \n produces a new line

#If you don’t want characters prefaced by \ to be interpreted as special characters,
# you can use raw strings by adding an r before the first quote
print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote

# String literals can span multiple lines
# One way is using triple-quotes: """...""" or '''...'''.

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
# note that the initial newline is not included (above)


#Strings can be concatenated  with the + operator
# and repeated with *
# 3 times 'un', followed by 'ium'
print (3 * 'un' + 'ium')

#Two or more string literals next to each other are automatically concatenated.
print ('py' 'thon')

print ('Put several strings within parentheses '
        'to have them joined together.')
# This only works with two literals though, not with variables or expressions

#If you want to concatenate variables or a variable and a literal, use +
prefix = 'Py'
print (prefix + 'thon')

# Strings can be indexed (subscripted),
# with the first character having index 0.
# There is no separate character type;
# a character is simply a string of size one

word = 'Python'
word[0]  # character in position 0

word[5]  # character in position 5

