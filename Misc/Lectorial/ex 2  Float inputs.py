import sys

sys.stdout.write ("Enter expense name: ")
expense_0_name = sys.stdin.readline().strip()

sys.stdout.write ("Enter expense amount: ")
expense_0_amount = float(sys.stdin.readline())


message = ""

message += "Expense 0 is " + expense_0_name
message += " which is $" + str(expense_0_amount)

sys.stdout.write("Expense 0 is " + expense_0_name + " which is " + str(expense_0_amount))
sys.stdout.write ("\n\n")
sys.stdout.write(message)
                 
# both messages produce the same output
