#Enter docstrings on each block of code
import sys

sys.stdout.write("Hello, We are your friendly budget consultants!")
sys.stdout.write("\n\nPlease answer the following questions. "+
                 "\nThe trolls downstairs will then let you know\n how much fun you are allowed this weekend.")

# justify variable name and datatype
# ---------------------------------------
# hourly rate of the user needs to be stored when retried from the user.
# The hourly rate variable was named hourly_pay_rate as this is a basic description of the value in a real world situation.
# I could have chosen to name it something else such as pay_rate, salary_per_hour, however,
# I found that using hourly_pay_rate would make the code easier to refer to and breakdown during testing, given there is only one pay rate in this program.
# The hourly_pay_rate helped to provide the best description of the input and value in this instance.
# I have chosen to save the variable data type as a float, as it can hold a decimal value if needed. I could have used an integer, however I realised that it would not accept decimal.

sys.stdout.write("\n\nWhat is your hourly rate: ")
hourly_pay_rate = float(sys.stdin.readline())

# justify the code block
# --------------------------------------
# while loop here will execute if the user has entered a negative number.
# I chose to use this code block as a negative number in the program would not produce a result and give an error. 
# The loop will continuosly prompt the user to enter a new number until it has received a positive, this action will allow the program to proceed to the next steps.

while (hourly_pay_rate < 0):
    sys.stdout.write("\nDude, how do you get a negative rate? - try again: ")
    sys.stdout.write("\nHow many hours have you worked this week: ")
    hourly_pay_rate = float(sys.stdin.readline())

# justify variable name and datatype
# ---------------------------------------
# hours worked of the user needs to be stored when retried from the user.
# The hours worked variable was named hours_worked as this is a basic description of the value in a real world situation.
# I could have chosen to name it something else such as number_of_hours_worked, week_hours, working_hours,
# I found that using hours_worked would make the code easier to refer to and breakdown during testing, given there is only one variable for hours worked in this program.
# The hours_worked helped to provide the best description of the input and value in this instance.
# I have chosen to save the variable data type as a float, as it can hold a decimal value if needed as the user may choose to enter half of an hour, in their answer.  

sys.stdout.write("\nHow many hours have you worked this week: ")
hours_worked = float(sys.stdin.readline())

# justify the code block
# --------------------------------------
# while loop here will execute if the user has entered a negative number.
# I chose to use this code block as a negative number in the program would not produce a result and give an error. 
# The loop will continuosly prompt the user to enter a new number until it has received a positive, this action will allow the program to proceed to the next steps.

while (hours_worked < 0):
    sys.stdout.write("\nDude, You have entered negative hours - try again: ")
    sys.stdout.write("\n\nWhat is your hourly rate: ")
    hours_worked = float(sys.stdin.readline())

# justify variable name and datatype
# ---------------------------------------
# The gross pay variable is a result of multiplying the hourly_pay_rate variable against the hours_worked variable.
# I chose to name the variable gross pay as this an accurate description of what the variable is, and the variable was easier to refer to.
# I could have chosen to name this variable pay_before_tax, pay, total_pay, not_nett_pay,
# but I felt that it wouldn't be suited in this situation given that it would not provide the same clarity of gross_pay.


gross_pay = (float(hourly_pay_rate*hours_worked))

# justify variable name and datatype
# ---------------------------------------
# This variable is called tax, tax is the most simplest and descriptive name I could come up with and is perfect, for what I am calculating in the code.
# I could have chosen another name such as taxation, tax_deduction, but as there is only one element of tax in this code, I chose to keep it simple.
# I also chose to keep the datatype as float to allow for decimal places, as this would produce a more accurate result in the end.
# An integer was considered, but the results were not as accurate. 

tax = (float(gross_pay*0.12))

# justify variable name and datatype
# ---------------------------------------
# the nett pay variable was named nett_pay as it is the result of subtracting gross_pay from tax, in a real world setting, we would normally call this nett pay.
# I have chosen nett_pay to accurately describe the value aswell as keep the name simple. I could have also called this variable nett, pay_after_tax, payment_deposited_into_bank,
# pay_less_after_tax, however, I think nett_pay is more suited in this instance.
# I also chose to keep the datatype as float to allow for decimal places, as this would produce a more accurate result in the end.
# An integer was considered, but the results were not as accurate. 

nett_pay = (float(gross_pay-tax))

# We need to print the results of the variables to the user.
sys.stdout.write("\nYou have earned a total of " + (str(round(gross_pay, 2))) + " " + "dollars this week." +
                 "\nThe amount of tax deducted will be " + (str(round(tax)))+ " " + "dollars." +
                 "\nThe amount deposited to your bank will be " + (str(round(nett_pay,2)))+ " " + "dollars after tax.")

# I have created 3 lists to present to the user, depending on how much many they have left over in the nett_pay variable.
# List 1  - lucky numbers 
lucky_numbers = [ 10, 52, 1, 6, 13]

# List 2 - fun that will cost less than 50
less_expensive_fun = ["Dinner at McDonalds", "Mini-golf", "Netflix", "Bowling"]

# List 3 - fun that will cost more than 50
expensive_fun = ["Shopping", "Dinner at a fancy restaurant", "Movies at the Cinema"]

# justify the condition
# --------------------------------------
# if statements below was created to print the lists applicable to the nett_pay result.
# I could have just used the if statement without the while loop, but I did not think the output result was as nice to read,
# and it would have sufficed without the while loop.
# a neat list at the end, printed once is easier to read for the user. 

if (nett_pay <=50): 
    sys.stdout.write("\nYou have no money for any real fun, but here are your lucky numbers")
    ff = 0
    
    while (ff < len(lucky_numbers)):
        sys.stdout.write("\n" + str(lucky_numbers[ff]))
        ff += 1

if (nett_pay >=50): 
    sys.stdout.write("\nYou have a few dollars to spare, here are some ideas:")
    lef = 0
    
    while (lef < len(less_expensive_fun)):
        sys.stdout.write("\n" + less_expensive_fun[lef])
        lef += 1

if (nett_pay >=100): 
    ef = 0
    
    while (ef < len(expensive_fun)):
        sys.stdout.write("\n" + expensive_fun[ef])
        ef += 1

