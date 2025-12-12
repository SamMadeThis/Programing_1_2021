t = 12345, 54321, 'hello!'
t[0]

t

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u

# Tuples are immutable:
t[0] = 88888

#DEFINE IMMUTABLE: unchanging over time or unable to be changed.

#OUTPUT TypeError: 'tuple' object does not support item assignment
