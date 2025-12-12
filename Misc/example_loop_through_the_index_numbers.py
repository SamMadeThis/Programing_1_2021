#You can also loop through the list items by referring to their index number.
#Use the range() and len() functions to create a suitable iterable.

thislist = ["apple", "banana", "cherry"]
thelist = ["blue", "brown", "black"]
for i in range(len(thislist)):
  print(thislist[i] +":" + thelist[i])
