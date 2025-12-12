import sys

valid = True
num1=0
while valid == True:
    if num1 == 0:
    #loop until the user enters a valid int
        sys.stdout.write ("Enter an int:")
        num1 = int(sys.stdin.readline())
        sys.stdout.write ("You entered :" + str(num1))
        valid = False #if this point is reached, x is a valid int
        if num1 > 0:
            sys.stdout.write ("\nMoving on to the next if statement")
        else:
            sys.stdout.write ("Try again: ")
