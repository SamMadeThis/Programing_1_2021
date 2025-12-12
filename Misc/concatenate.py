import sys

name = "Samantha Brayne"
answer = 2 + 3

sys.stdout.write ("Hello my name is ")
sys.stdout.write (name + "...\n")
#converting the int answer as a string just to display rather than convert the int within the variable as a string
# if you need to use the INT at another time it wouldn't work
sys.stdout.write ("\nAnswer is "+ str(answer) + " simple addition of INT")

answer = 3 * 2
sys.stdout.write ("\nAnswer is "+ str(answer) + " repeats the INT 3 times")
answer = 3 * "2" #not best practice to repeat strings
sys.stdout.write ("\nAnswer is "+ str(answer) +" repeats the string 3 times")


answer = 3 /0 # Will cause an error as you cannot divide by 0
sys.stdout.write ("\nAnswer is "+ str(answer) )


