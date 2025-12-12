# 2.3.3 Regarding break and continue statements, and else clauses on loops
# Avoiding spaghetti code - Similarly, when programming,
# we avoid certain statements so as to increase the readability
# of our code and to be polite to our fellow programmers.
# In this task, you’ll learn about break and continue statements,
# and how they can cause problems in programs.

# break statements allow us to exit for-loops early before the for-loop has finished executing entirely.
# They can be used in conjunction with if statements.
# -----------------------------------------------------
# For example, this program features a list of numbers.
# The winning number is the first number that is over 18:
##guess = [1, 2, 7, 10, 13, 17, 19, 7, 3, 36, 5]
##for x in guess:
##    if x > 18:
##        print(x,"is the winning number")
##        break
##    else:
##        print(x, "is not a winner")
# As soon as the winning number is identified, the loop stops even though the for-statement commands we go through all of the strings in the list.
# -------------------------------------------------------

#break statements in more complex programs are considered bad practice and inelegant as they can lead to badly structured code known as “spaghetti code”.
# Similarly, continue statements, which involve a loop skipping over the start of the next iteration from the middle of a loop’s body,
# are also considered bad practice.
#break and continue statements are also found in C and Java programming languages.
# They are fundamental concepts, although not ones we should use.
# Python also has an else clause whereas the other languages only use else with if statements.
# As we will not be using break or continue in loops, for now the else-clause will also not be used.

# ---------Reading -----------------------------------------------------
# examples from the documentation to keep building your understanding of the fundamentals of programming [Section 4.4 only].
# link: https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops

##for n in range(2, 10):
##    for x in range(2, n):
##        if n % x == 0:
##            print(n, 'equals', x, '*', n//x)
##            break
##    else:
##        # loop fell through without finding a factor
##        print(n, 'is a prime number')

# -----------------------------
# % used to perform concatenation of strings together. allows you to format a value inside a string.
# it is used to incorporate another string with a string. it automatically provides type conversion from value to string.

# When used with a loop, the else clause has more in common with the else clause of a try statement than it does with that of if statements
# a try statement’s else clause runs when no exception occurs, and a loop’s else clause runs when no break occurs.


# For more on the try statement and exceptions, see Handling Exceptions.
# link: https://docs.python.org/3/tutorial/errors.html#tut-handling

# The continue statement, also borrowed from C, continues with the next iteration of the loop:
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)


## -----------------------------------------------------------
## Acitivity question:What do you suppose the % operator does?
    
## answer :The % operator (also known as the modulus operator) is applied to integers and returns the remainder when the first operand is divided by the second.
# In the application in the documentation, the operator is used to identify integers that have factors and which are therefore not a prime number.
