Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> squares = [1, 4, 9, 16, 25]
>>> squares[0]
1
>>> # indexing returns the item
>>> squares[-1]
25
>>> squares[-3:]  # slicing returns a new list
[9, 16, 25]
>>> squares[:]
[1, 4, 9, 16, 25]
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> #Lists also support operations like concatenation
>>> # as shown above
>>> # Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:
>>> cubes = [1, 8, 27, 65, 125]
>>> # something's wrong here
>>> 4 ** 3
64
>>> # the cube of 4 is 64, not 65!
>>> cubes[3] = 64  # replace the wrong value
>>> cubes
[1, 8, 27, 64, 125]
>>> # You can also add new items at the end of the list, by using the append() method (we will see more about methods later):
>>> cubes.append(216)  # add the cube of 6
>>> cubes.append(7 ** 3)  # and the cube of 7
>>> cubes
[1, 8, 27, 64, 125, 216, 343]
>>> cubes.append(42)
>>> cubes
[1, 8, 27, 64, 125, 216, 343, 42]
>>> #
>>> # Assignment to slices is also possible, and this can even change the size of the list or clear it entirely
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> # replace some values
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> # now remove them
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> # clear the list by replacing all the elements with an empty list
>>> letters [:] = []
>>> letters
[]
>>> # The built-in function len() also applies to lists:
>>> letters = ['a', 'b', 'c', 'd']
>>> len(letters)
4
>>> # It is possible to nest lists (create lists containing other lists), for example:
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> 
KeyboardInterrupt
x[0]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
>>> x [1][0]
1
>>> 