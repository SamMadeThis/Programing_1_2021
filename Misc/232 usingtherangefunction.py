words = ['cat', 'window', 'defenestrate']

##for w in range(0,len(words)):
##  print(w,len(words[w]))

# Q1 The first argument to range() is 0. What does this do?
# ------------
# output
# 0 3
# 1 6
# 2 12
# -----------
# range starts from 0 which prints the length of Cat on the first line
# second line is the next position 1 and prints the length on window
# third line is position 2 which prints the length of defenestrate
# -------------------------------------------------------------------


for w in range(0,len(words),2):
    print (w,len(words[w]))


# Q2 The second argument to range () is (len(words). What does this do?
# --------------------
# output:
# 0 3
# 2 12
# ---------------------
# First line outputs the position 0 and length of cat
# second line outputs the position of 2 and length of defenestrate
