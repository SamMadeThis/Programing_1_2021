import sys
import backend

# (Justification comment for code block below)
# the purpose of this function is to initialize the string data input from
# the user in order to keep the program running without error from blank
# user input
def get_str(prompt: str)->str:
    sys.stdout.write(prompt)
    sys.stdout.flush()
    # (Justification comment for variable below)
    # Alternative names I could have used are user_input or choice, however
    # I wanted to clearly show that the value will be returned rather than
    # the input variable as it will used within multiple variable inputs.
    value = sys.stdin.readline().strip()
    # (Justification comment for condition below)
    # while the length of the value (which will be input saved to a variable)
    # length is 0 the while loop will continue to prompt for input until the
    # condition is false. 
    while(len(value)==0):
        sys.stdout.write("Error! Input cannot be blank. Re-enter:  ")
        sys.stdout.flush()
        # (Justification comment for variable below)
        # Alternative names I could have used are user_input or choice, however
        # I wanted to clearly show that the value will be returned rather than
        # the input variable as it will used within multiple variable inputs.
        value = sys.stdin.readline().strip()
    return value

# (Justification comment for code block below)
# the purpose of this function is to initialize the int type data input
# from the user in order to keep the program running without error from
# blank user input.
def get_int(prompt:str)->str:
    # (Justification comment for variable below)
    # Alternative names I could have used are user_input or choice, however
    # I wanted to clearly show that the value will be returned rather than
    # the input variable as it will used within multiple variable inputs.
    value=None
    # (Justification comment for condition below)
    # while the value is None (which will be input saved to a variable)
    # the while loop will continue to prompt for input until the
    # condition is false. 
    while (value ==None):
        try:
            # (Justification comment for variable below)
            # Alternative names I could have used are user_input or choice, however
            # I wanted to clearly show that the value will be returned rather than
            # the input variable as it will used within multiple variable inputs.
            # Valie is INT as is required on some of the input to allow the
            # operations run correctly. 
            value=int(get_str(prompt))
        except:
            # (Justification comment for variable below)
            # Alternative names I could have used are input or input_message
            # however I thought prompt represented the context of the variable
            # its purpose is to prompt the user to re-enter input. The data type
            # is string as text is required to communicate to the user, INT or
            # Float would not provide the same output without a lot of difficulty.
            prompt="That wasn't right. Re-enter: "
    return value

# (Justification comment for code block below)
# the purpose of this function is to initialize the float type data input
# from the user in order to keep the program running without error from
# blank user input
def get_float(prompt: float):
    # (Justification comment for variable below)
    # Alternative names I could have used are user_input or choice, however
    # I wanted to clearly show that the value will be returned rather than
    # the input variable as it will used within multiple variable inputs.
    value=None
    # (Justification comment for condition below)
    # while the value is None (which will be input saved to a variable)
    # the while loop will continue to prompt for input until the
    # condition is false. 
    while (value ==None):
        try:
            # (Justification comment for variable below)
            # Alternative names I could have used are user_input or choice,
            # however, I wanted to clearly show that the value will be
            # returned rather than the input variable as it will used
            # within multiple variable inputs.
            # Value is FLOAT as is required on some of the input to allow the
            # operations run correctly. 
            value=float(get_str(prompt))
        except:
            # (Justification comment for variable below)
            # Alternative names I could have used are input or input_message
            # however I thought prompt represented the context of the variable
            # its purpose is to prompt the user to re-enter input. The data type
            # is string as text is required to communicate to the user, INT or
            # Float would not provide the same output without a lot of difficulty.
            prompt="That wasn't right. Re-enter: "
    return value

# (Justification comment for code block below)
# the purpose of this function is to initialize the float type data as a
# positive float input from the user in order to keep the program running
# without error from blank user input
def get_positive_float(prompt:str)->str:
    # (Justification comment for variable below)
    # Alternative names I could have used are user_input or choice, however
    # I wanted to clearly show that the value will be returned rather than
    # the input variable as it will used within multiple variable inputs.
    value= get_float(prompt)
    # (Justification comment for condition below)
    # while the value is less than zero (which will be input saved to a variable)
    # the while loop will continue to prompt for input until the
    # condition is false. 
    while (value<0):
        # (Justification comment for variable below)
        # Alternative names I could have used are user_input or choice, however
        # I wanted to clearly show that the value will be returned rather than
        # the input variable as it will used within multiple variable inputs.
        # data type is float as this required to run some of the
        # operations correctly. 
        value = get_float("Input must be positive. Re-enter: ")
    return value

# (Justification comment for code block below)
# get menu choice is a function display the menu options to the user and
# get their choice to perform an operation. I could have combined the menu
# with the main function however it was easier to read and maintain in
# seperate functions.
# Alternately, I could just have written the menu into the main but I
# thought this was suitable considering the readability. 
def get_menu_choice():
    """
    Menu will prompt the user for an option to trigger an operation listed
    in the main. 
    """
    # (Justification comment for variable below)
    # Alternative names I could have used are program_menu, program_options,
    # however menu is more suitable and keeps the code easier to read.
    # Data type is string to allow the text to be printed to user and
    # inform them of the options available. I dont think it would be
    # appropriate to use INT or Float to perform this work as we would not
    # get the same output. 
    menu = "\n====================================================\n"
    menu += "\n\tWelcome to Monopoly Industries Banking App\n\n"
    menu += "\t[A]dd account\n"
    menu += "\t[V]iew your accounts\n"
    menu += "\t[W]ithdrawal\n"
    menu += "\t[D]eposit \n"
    menu += "\t[L]oad data\n"
    menu += "\t[S]ave data\n"
    menu += "\tE[x]it\n"
    menu += "\n====================================================\n"
    sys.stdout.write(menu)
    # (Justification comment for variable below)
    # Alternative names I could have used are program_menu, program_options,
    # however menu is more suitable and keeps the code easier to read.
    # Data type is string to allow the text to be printed to user and
    # inform them of the options available. I dont think it would be
    # appropriate to use INT or Float to perform this work as we would not
    # get the same output. To reduce duplication of lower on if statement
    # blocks in the main(), I have written it here to lower all input to
    # trigger the code blocks.
    menu=menu.lower()
    # (Justification comment for variable below)
    # Alternative names I could have used are options, user_input, however
    # for consistancy I chose to keep choice as it describes the user choice
    # of input. get_str is called in this variable as to ensure the input is
    # not blank and break the program. 
    choice = get_str("Enter an option: ").lower()
    return choice

# (Justification comment for code block below)
# The purpose of this function is to get the withdrawal input from the user and
# validate the input before sending the data to the backend to change the
# specified variables as required in this transasction. 
def get_withdrawal():
    # (Justification comment for variable below)
    # Alternative names I could have used are bank_account_number,
    # however I chose to abbreviate the name to keep the code easier to read.    
    bank_acc_num = get_int("Enter your account number: ")
    # (Justification comment for variable below)
    # Alternative names I could have used are amount, withdrawal or x,
    # I thought this name was sufficient as it accurately described the
    # context of the variable.
    withdraw_amount = get_positive_float("Enter withdraw amount: ")
    # (Justification comment for condition below)
    # The backend function will return a boolean to confirm
    # if the operation has completed successfuly.
    # The if statement below will trigger and print a message to the user
    # and confirm the results. 
    if (backend.withdrawal(bank_acc_num,withdraw_amount)==True):
        withdrawal_confirmation = "\nYou have withdrawn $" 
        withdrawal_confirmation += f'{withdraw_amount:.2f}' 
        withdrawal_confirmation += " from account "+str(bank_acc_num )
        sys.stdout.write(withdrawal_confirmation)
    # (Justification comment for condition below)
    # The backend function will return a boolean to confirm
    # if the operation has completed successfuly.
    # The if statement above will trigger and print a message to the
    # user and confirm the results.
    # The elif will confirm an no matches found if unsucessful. 
    elif (backend.withdrawal(bank_acc_num,withdraw_amount)==False):
        withdrawal_error = "An Error has occured.\n\n"
        withdrawal_error += "Please check your account number and\n"
        withdrawal_error += "ensure that you have sufficient balance.\n"
        sys.stdout.write(withdrawal_error)
        
# (Justification comment for code block below)
# The purpose of this function is to get the deposit input from the user and
# validate the input before sending the data to the backend to change the
# specified variables as required in this transasction.        
def get_deposit():
    # (Justification comment for variable below)
    # Alternative names I could have used are bank_account_number,
    # however I chose to abbreviate the name to keep the code easier to read.     
    bank_acc_num = get_int("Enter your account number: ")
    # (Justification comment for variable below)
    # Alternative names I could have used are amount, deposit or x,
    # I thought this name was sufficient as it accurately described the
    # context of the variable.
    deposit_amount = get_positive_float("Enter deposit amount: ")
    # (Justification comment for condition below)
    # The backend.deposit function will return a boolean to confirm
    # if the operation has completed successfuly.
    # The if statement below will trigger and print a message to the user
    # and confirm the results. 
    if (backend.deposit(bank_acc_num, deposit_amount)==True):
        deposit_confirmation = "\nYou have deposited $"
        deposit_confirmation +=f'{deposit_amount:.2f}' 
        deposit_confirmation += " in to account "+str(bank_acc_num)
        sys.stdout.write(deposit_confirmation)
    # (Justification comment for condition below)
    # The backend.deposit function will return a boolean to confirm
    # if the operation has completed successfuly.
    # The if statement above will trigger and print a message to the
    # user and confirm the results.
    # The elif will confirm an no matches found if unsucessful. 
    elif (backend.deposit(bank_acc_num, deposit_amount)==False):
        # (Justification comment for variable below)
        # Alternative names I could have used are x or account_matches,
        # however I thought matches was sufficient as it described the context
        # of data saved to the variable.
        matches_error = "\nNo matches found, " 
        matches_error +="please check your account number and try again later"
        sys.stdout.write(matches_error)
    
def get_save_filename():
    # (Justification comment for variable below)
    # Alternative names I could have used are file,
    # file_object or x, however I thought filename
    # was more suitable as it describes the
    # contents of the variable.
    filename = get_str("Enter file name: ")
    # (Justification comment for condition below)
    # The backend function will return a boolean to confirm
    # if the operation has completed successfuly.
    # The if statement below will trigger and print a message to the user
    # and confirm the results. 
    if (backend.save_data(filename) == True):
        sys.stdout.write("\nFile saved successfully")
    # (Justification comment for condition below)
    # The backend function will return a boolean to confirm
    # if the operation has completed successfuly.
    # The if statement above will trigger and print a message to the
    # user and confirm the results.
    # The elif will confirm an no matches found if unsucessful. 
    else:
        sys.stdout.write("\nError - File not saved")

# (Justification comment for code block below)
# get_new_account is a function to recieve the account details and send the
# account details to the backend and append the data into the lists.
# Alternatively, I could have just written the prompts below into the
# corresponding if statement of the menu. However, if the menu were updated
# with additional code it would be difficult to maintain.     
def get_new_account():
    # (Justification comment for variable below)
    # Alternative names I could have used are acc_num or number, however
    # account_number was more suitable to represent the context saved in
    # the variable. get_int is required as the account numbers are stored as
    # INT which is consistant with other banks. 
    account_number = get_int("Enter your account number: ")
    # (Justification comment for variable below)
    # Alternative names I could have used are acc_name or name, however
    # account_name was more suitable to represent the context saved in
    # the variable.
    # get_str is required on this input to ensure the data is stored as string
    # consistant throughout the program. There is no real need on the backend
    # for a string data type however it would make the account easier for the
    # customer to recognise by putting a name to it. 
    account_name = get_str("Enter the account name: ")
    # (Justification comment for variable below)
    # Alternative names I could have used are opening_balance or money, however
    # balance was more suitable to represent the context saved in
    # the variable.
    # get_float is required as the account balances are stored as
    # float to allow addition and subtraction to decimal values such as normal
    # money transactions which is consistant with other banks. 
    balance = get_float("Enter an opening balance: ")
    # (Justification comment for condition below)
    # The backend function will return a boolean to confirm
    # if the operation has not completed due to an error.
    # The if statement above will trigger and print a message to the
    # user and confirm the results.
    if (backend.add_account(account_number, account_name, balance)==False):
        sys.stdout.write("Error - Try again later :")

# (Justification comment for code block below)
# The purpose of this function is to print a list of all of the details
# currently saved within the account lists on screen to the user.
# As mentioned before it is possible to include this code block within the
# if statement of main() however if there were more code added to the menu
# it would become difficult to maintain the code down the track.
# This function was written into the frontend due to the text required to
# be displayed on screen to the user, so I classed this as user interface
# rather than backend operation. 
def display_accounts():
    # (Justification comment for variable below)
    # Alternative names I could have used are num_accounts, or
    # len_account_ names however to keep the code easy to read and
    # maintained I chose to use this name as it describes the content
    # of the variable.
    # Alternatively, I could have used INT and written a number however it
    # made sense just to get the number of items currently within the list
    # so the loop only runs the necessary times required perform the operation.
    len_accounts = len(backend.account_names)
    # (Justification comment for variable below)
    # Alternative names I could have used are i, x or account_index,
    # however I think index is sufficient as it describes the value within
    # the loop. 
    index = 0
    # (Justification comment for variable below)
    # Alternative names I could have used are print_accounts
    # or display_accounts, but I thought this was sufficient
    # and chose to use view accounts and keep
    # the code consistant with the menu options. 
    view_accounts = "\n\tView all accounts\n\n"
    # (Justification comment for condition below)
    # It made sense just to get the number of items currently within the
    # list so the loop will only run the necessary amount of times
    # required to fully perform the operation. So if the len_accounts
    # is greater than zero this code block will run. We do not need this
    # to run if there are no items in the lists. 
    if len_accounts > 0:
        # (Justification comment for condition below)
        # It made sense just to get the number of items currently within the
        # list so the loop will only run the necessary amount of times
        # required to fully perform the operation.
        while (index<len_accounts):
            view_accounts += "\tAccount Number: "
            view_accounts += str(backend.account_numbers[index]) + "\n"
            view_accounts += "\tAccount Name: "+ backend.account_names[index]
            view_accounts += "\n\tAccount Balance: $"
            view_accounts += f'{backend.account_balances[index]:.2f}' +"\n\n"
            index +=1
        # (Justification comment for variable below)
        # Variable named to format the string saved to view_accounts,
        # the name was sufficient as it described its function in this instance.
        # Alternatively, I could have called it display_accounts, x however
        # I thought display was consistant with the names currently used within this program. 
        display = view_accounts.center(50)
        sys.stdout.write(display )
    # (Justification comment for condition below)
    # Following from the previous if statement if there are no items in the list
    # this code block will be triggered to confirm to the user that there are no
    # accounts found in the lists they wish to display.       
    elif len_accounts == 0:
        display ="\nNo accounts found."
        sys.stdout.write(display)
  
# (Justification comment for code block below)
# the purpose of this function is to run the main programme and trigger the
# operations on request by the user as required.
def monopoly_bank_main():
    choice = get_menu_choice()
    # (Justification comment for condition below)
    # The condition on the while loop is if choice is not x, this means the
    # loop will continue to run if the choice, which is the user input
    # enters x to exit the program.
    # x is listed an option to exit. 
    while (choice!="x"):
        sys.stdout.write("\n")
        # a is listed as an operation in the menu.
        # That will trigger this if statement.
        if (choice=="a"):
            get_new_account()
        # v is listed as an operation in the menu.
        # That will trigger this if statement.
        elif (choice=="v"):
            display_accounts()
        # l is listed as an operation in the menu.
        # That will trigger this if statement.
        elif (choice=="l"):
            # (Justification comment for variable below)
            # Alternative names I could have used are file_name or f
            # however I thought this was sufficient for this purposes and describes
            # its purpose and the context of the data saved to the variable.
            filename = get_str("Enter filename: ")
            # (Justification comment for condition below)
            # if backend.load_data(filename) returns True than it means the
            # operation has run successfully and therefor, once this triggered
            # the user will receive confirmation. Its not technically necessary,
            # however in order to provide a good experience for the user, it make sense to include this. 
            if (backend.load_data(filename)==True):
                sys.stdout.write("\nFile loaded successfully.")
            # (Justification comment for condition below)
            # Following on from the justification above, the else statement
            # will print an error as it will mean the operation did complete successfully. 
            else:
                # (Justification comment for variable below)
                # multiline string saved to variable, the load error is an accurate
                # description on the context of the data saved to this variable.
                # Alternatively, I could have used error_msg, x, or load_confirmation
                # but I thought load_error was sufficient due to the context.
                load_error = "\nError: Could not load file."
                load_error +="\nCheck the file and try again"
                sys.stdout.write(load_error)
            
        # s is listed as an operation in the menu.
        # That will trigger this if statement.
        elif (choice=="s"):
            get_save_filename()
            
        # d is listed as an operation in the menu.
        # That will trigger this if statement.
        elif (choice=="d"):
            get_deposit()
       
        # w is listed as an operation in the menu.
        # That will trigger this if statement.
        elif (choice=="w"):
            get_withdrawal()
        else:
            sys.stdout.write("\nInvalid choice, try again: ")
        choice = get_menu_choice()
    sys.stdout.write("\nGoodbye!")
        
monopoly_bank_main()
