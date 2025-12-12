#The reverse operation is also possible:
t = 12345, 54321, 'hello!'
x, y, z = t

#TYPE t
#OUTPUT (12345, 54321, 'hello!')
#TYPE x
#OUTPUT 12345
#TYPE y
#OUTPUT 54321
#TYPE z
#OUTPUT 'hello!'

# This is called sequence unpacking.
# Works for any sequence on the right hand side.
# Sequence unpacking requires that there are as many
# variables on the left side of the equals sign as
# there are elements in the sequence.
# Note that multiple assignment is really just a
# combination of tuple packing and sequence unpacking.
