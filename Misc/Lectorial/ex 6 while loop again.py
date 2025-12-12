import sys

expense_names = []
expense_amounts_in_cents = []

sys.stdout.write("Enter expense name: ")
expense_name=(sys.stdin.readline().strip())
while (expense_name != ""):      
    sys.stdout.write ("Enter ammount for " + expense_name+" in cents: ")
    expense_amount_in_cents = int(sys.stdin.readline())
    while (expense_amount_in_cents < 0):
        sys.stdout.write("Error! Enter a positive amount: ")
        expense_amount_in_cents = int(sys.stdin.readline())

    expense_names.append( expense_name)
    expense_amounts_in_cents.append(expense_amount_in_cents)

    #Asking for the next input
    sys.stdout.write("Enter expense name: ")
    expense_name = sys.stdin.readline().strip()

#Much later........

# dont display entire lists
sys.stdout.write(str(expense_names) + "\n")
sys.stdout.write(str(expense_amounts_in_cents) +"\n")
