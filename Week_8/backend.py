account_numbers = []
account_names = []
account_balances = []

# (Justification comment for code block below)
# Function created to add new account details to the lists.
# add_account was suitable as the name in this instance as it describes the
# operation of the function.
# Alternatively, I could have not created a function and left this peice in
# the front end menu however, it would become too complex if there were
# more additions in the menu. It made sense to create its own function to
# perform this action to easily maintain the code. 
def add_account(account_number:int, account_name:str, balance:float):
    account_numbers.append(account_number)
    account_names.append(account_name)
    account_balances.append(balance)

    
# (Justification comment for code block below)
# Function created to load data from an existing file external to the
# program and append the data into the lists of the program.
# Alternatively, I could have not created a function and left this peice in
# the front end menu however, it would become too complex if there were
# more additions in the menu. It made sense to create its own function to
# perform this action to easily maintain the code.
# filename was included as a parameter from the front end to allow the user
# to choose the filename. I could have also just had one function to combine
# the prompt to choose a filename and then load the data into the lists but
# I thought it would be more suitable to keep as much of the strict operations
# in the backend as there is alot of functions already required to sit in the
# frontend for consistancy.
def load_data(filename:str)->bool:
    try: 
    # (Justification comment for condition below)
    # while lines is not blank the loop will continue to read the data on
    # the file and append the details found in the lists.
    # Alternatively I could have used the example found in wk 6 Expense manager,
    # as follows:
    ### with open("expenses.csv", "r") as file_object:
    ###    for line in file_object:
    # However, I chose to use the condition below as that is within the spec of
    # this assignment. 
    
        file_object = open(filename, "r") 
        line = file_object.readline().strip()
        while (line != ""):
            fields=line.split(",")
            account_number=int(fields[0])
            account_name=fields[1]
            balance=float(fields[2])
            add_account(account_number, account_name, balance)
            line = file_object.readline().strip()
        file_object.close()
        saved=True
    except:
        saved=False
        
    return saved


def deposit(bank_acc_num: int,deposit_amount: float)->bool:
    matches = False
    index = 0
    len_accounts = len(account_numbers)

    while (index < len_accounts):
        if (bank_acc_num == account_numbers[index]):
            account_balances[index] += deposit_amount
            matches = True
        index+=1
    return matches

def save_data(filename:str)->bool:
    """ exception handling code block
    """
    try:
        # (Justification comment for variable below)
        # Alternative names I could have used are x, lines_to_write,
        # however in this instance I thoughts lines was sufficient
        # as its purposes is to just save data that will be written
        # in to the file. The name is a description of the contents
        # of the variable.
        lines = ""        
        # (Justification comment for variable below)
        # Alternative names I could have used are account_names,
        # len_account_names, but I chose to use num_accounts,
        # to show that the variable stores the number of accounts
        # that exist. 
        num_accounts=len(account_names)
        # (Justification comment for variable below)
        # Alternative names I could have used are a, x, index,
        # however as this is a simple while loop it was sufficient to
        # use i as the variable to store the number each loop ran until
        # the condition of the  while loop is false.
        acc_id=0
        # (Justification comment for condition below)
        # It made sense just to get the number of items currently within the
        # list so the loop will only run the necessary amount of times
        # required to fully perform the operation.
        while(acc_id<num_accounts):
            lines += str(account_numbers[acc_id])+","
            lines +=account_names[acc_id]+","
            lines +=f'{account_balances[acc_id]:.2f}'+"\n"
            acc_id+=1
        file_object=open(filename,"w")
        file_object.write(lines + "\n")
        file_object.close()
        saved=True
    except:
        saved=False
    return saved
        
def withdrawal(bank_acc_num:int,withdraw_amount:float)->bool:
    matches = 0
    index = 0
    balance_check = 0
    len_accounts = len(account_numbers)
    while (index < len_accounts):
        if (bank_acc_num == account_numbers[index]):
            matches+=1
            if (withdraw_amount <= account_balances[index]):
                balance_check += 1     
        index+=1
    index=0
    if matches > 0 and balance_check > 0:
        while (index <len_accounts):
            if (bank_acc_num == account_numbers[index]) :
                account_balances[index] -= withdraw_amount
            index+=1
        balance = True
    elif balance_check == 0 or matches == 0:
        balance = False
    return balance


        
