# Task
# 1 - The function should take an integer from the user and then return it to the user. (Consider the example earlier in the task that uses the weekID variable.)
# 2 - Your code should use stdout where possible.
# 3 - Your function should be named display.
# 4 - Before your function is called, your program should display the words “Hi there” to the user.


import sys
def display(i):
    a, b = 0, 1
    while i>0:
        a, b = b, a+b
        i-=i
return a
sys.stdout.write("Enter your age: ")
i = int( sys.stdin.readline() )
answer = display(i)
sys.stdout.write( str(answer) + " is at "+str(i))





