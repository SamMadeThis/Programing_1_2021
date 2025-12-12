# 2.3.2 Using the range() function
# complete this task by trying out the statements in the Python documentation.
# 4.3. The range() Function
# link: https://docs.python.org/3/tutorial/controlflow.html#the-range-function

##for i in range(5):
##    print(i)

# generates arithmetic progressions
# The given end point if never part of the generated sequence
# the example above has a range of 5 - if we change it 10 it will generate 10 values
# it is possible to let the range start at another number
# OR specify a different increment

# examples of starting the range from another number
# ---------------------------
# example 1
##for i in list(range(5, 10)):
##            [5, 6, 7, 8, 9]
##            print (i)

# -----------------------
# example 2
#
##for i in list(range(0, 10, 3)):
##    [0, 3, 6, 9]
##    print (i)
# ------------------------
# example 3
##
##for i in list(range(-10, -100, -30)):
##    [-10, -40, -70]
##    print (i)
# ------------------------



# To iterate over the indices of a sequence,
# you can combine range() and len() as follows:

##a = ['Mary', 'had', 'a', 'little', 'lamb']
##for i in range(len(a)):
##    print(i, a[i])


## In most such cases, however,
# it is convenient to use the enumerate() function,
# see Looping Techniques.
# -----------------------------------------------

# A strange thing happens :

##for i in range(10):
##    print (i)

# if you just print a range, the object returned by range() behaves as if it is a list, but it is not.
# It is an object which returns the successive items of the desired sequence when you iterate over it, but it doesn’t really make the list, thus saving space.
# An object is iterable, that is, suitable as a target for functions and constructs that expect something from which they can obtain successive items until the supply is exhausted.

# the for statement is such a construct, while an example of a function that takes an iterable is sum():
##sum(range(4))  # 0 + 1 + 2 + 3

