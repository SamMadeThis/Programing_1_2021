import sys

expense_names = []
expense_amounts_in_cents = []


sys.stdout.write("Enter expense name: ")
expense_names.append(sys.stdin.readline().strip())

sys.stdout.write ("Enter expense amount in cents: ")
expense_amount_in_cents = int(sys.stdin.readline())
if (expense_amount_in_cents < 0):
    expense_amount_in_cents = 0
expense_amounts_in_cents.append(expense_amount_in_cents)


message = ""

message += "Expense 0 is " + expense_names [0]
message += " which is $" + str(expense_amounts_in_cents[0]/100)

sys.stdout.write("Expense 0 is " + expense_names [0] + " which is " + str(expense_amounts_in_cents[0]))
sys.stdout.write ("\n\n")
sys.stdout.write(message)
                 
# both messages produce the same output

