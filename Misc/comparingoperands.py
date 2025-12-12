import sys

# comparison of values assigned to cheque and savings 
cheque = 12
savings = 12
# do i need more money in my bank?
bank_account = cheque
bills = 12

if  cheque == savings :
  sys.stdout.write("Both bank accounts are about the same... ")
if cheque > savings:
  sys.stdout.write("You need to work on your savings! ")
if cheque < savings:
  sys.stdout.write("You need to work on your cheque account! ")


if bills > bank_account:
  sys.stdout.write("You need more money to pay the bills!")
if bills < bank_account:
  sys.stdout.write("You have enough money to pay the bills! ")
