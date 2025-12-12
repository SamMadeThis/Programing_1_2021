import sys

sys.stdout.write("Enter your age ")

# justify variable name and datatype
# ---------------------------------------
# age of the user needs to be stored when retrieved from the user
# age was used for the variable as a name, alternative names for the age
# variable can be years_spent_on_earth, rotations_around_sun, a, user_age
# driver_age, however, I found that age was easier to refer to, given that
# there are no other age related variables needed.
# The datatyoe that was used for age is an int (integer), as its meant to
# hold a whole number to represent that age of the user. An alternative
# datatype would be a float, however, in this particular program, a whole
# number is more suited for the user's age.

age = int(sys.stdin.readline())

# justify the code block
# --------------------------------------
# while is used to force repition if user enters a negative age
# alternatively, I could have used a for loop, however, the while
# is more suited here in this code block as the loop will end when age
# is positive

while (age < 0):
    sys.stdout.write("Age cannot be negative - try again: ")
    age = int(sys.stdin.readline())
    

# justify the condition
# --------------------------------------
# an if statement is used to control which message would be displayed to
# the user depending on their age.
# Alternatively this could also be written such that if age is less than
# 18, then they cannot drive, else they can. It can be written as not(age<18)

if (age >= 18):
    sys.stdout.write("\nCan drive")
else:
    sys.stdout.write("\nCannot drive")
