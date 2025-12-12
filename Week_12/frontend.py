import sys

# (Justification comment for code block below)

# As the spec requires a backend and frontend this class is neccessary to meet
# the requirements.
# The app.py will call the frontend and without this class that code would
# not run without error.

# The alternative could be just to create a function called FrontEnd but the
# naming convention would not follow the standard camel case.

# The functions listed in the class is listed in logical order, but that is
# not exactly required as the functions will run when called.
# The constructor includes:
#  1) The backend parameter which will be received from app.py.
#  2) The backend is saved in a variable.
#  3) The csv file will try to load and then run the UI.
# Next is the UI listed in the class and then input validations are then listed thereafter.

class FrontEnd:
    # (Justification comment for code block below
    # The closest alternative to creating this code block is a function but as
    # __init__ is a specific inbuilt function in python which calls
    # automatically when the class is called there really isnt an equal
    # alternative.

    # The parameter includes self and backend. Backend is received from app.py and then saved to a variable.
    # The csv file will try to load and then the UI will be called.
    # No other code is neccessary to be included in this code block to meet the spec requirements.

    def __init__(self, backend:str):
        
        # (Justification comment for variable below)
        # Variable created to save the information passed
        # from app.py it will specify the backend module and this variable will
        # be used when operations are required from that module.
        # Alternatively I could have called is self.__backendmanager or
        # self.__backendmodule but wanted to keep it simple and easy to read
        # in this instance. I did not want to include any details in the frontend
        # that was not required. As self is called in the backend module I also
        # used self and made the instance hidden with the double underscores.

        self.__backend = backend
        
        # (Justification comment for code block below)
        # try and except are used incase there are errors from the backend
        # that may need to be communicated to user in the program.
        # If try and except were not used and there was an error raised it would stop the program.
        # I dont think there are alternatives to the try/except,
        # I could have also specified another action to take such as loading a backup file to run the program. 

        try:
            self.__backend.load_data()
        
        # (Justification comment for code block below)
        # try and except are used incase there are errors from the backend
        # that may need to be communicated to user in the program.
        # If try and except were not used and there was an error raised it would stop the program.
        # I dont think there are alternatives to the try/except,
        # I could have also specified another action to take such as loading a backup file to run the program. 

        except:
            sys.stderr.write("Error cannot load file")
        self.monopolyUI()
        
    # (Justification comment for code block below)
    # MonopolyUI is named as the specific function to run the frontend
    # operations in the program.
    # Alternatively I could have called is User_Interface, frontend_ui
    # or similiar but I thought it was more suitable to use this name
    # to keep it consistant following the theme of this application.

    # This code block is neccessary to meet the spec requirements of
    # the assignment.
    # This function will deal with the backend and not the
    # BankAccounts class.
    
    # As shown in my previous assignment the alternative to creating this
    # function within the class is to have the function on its own
    # outside of the class.

    # The statements inside will communicate with the user and take input
    # to carry out the operations included in the menu.

    def monopolyUI(self):
        
        # (Justification comment for variable below)
        # Alternative names I could have used are program_menu, program_options,
        # however menu is more suitable and keeps the code easier to read.
        # Data type is string to allow the text to be printed to user and
        # inform them of the options available. I dont think it would be
        # appropriate to use INT or Float to perform this work as we would not
        # get the same output.
        
        menu =  "\n========================================\n\n"
        menu += "Monopoly Bank App V.2 \n"
        menu += "\n========================================\n"
        menu += "\t[V]iew your accounts\n"
        menu += "\t[A]dd new account\n"
        menu += "\t[W]ithdrawal\n"
        menu += "\t[D]eposit \n"
        menu += "\t[S]ave to a new file\n"
        menu += "\tE[x]it\n"
        menu += "\n========================================\n"
        menu += "Enter option: "
        
        # (Justification comment for variable below)
        # Alternative names I could have used are options, user_input, however
        # for consistancy I chose to keep choice as it describes the user choice
        # of input. get_str is called in this variable as to ensure the input is
        # not blank and break the program.
        
        choice = FrontEnd.__get_str(menu).lower()
        
        # (Justification comment for condition below)
        # The condition on the while loop is if choice is not x, this means the
        # loop will continue to run if the choice, which is the user input
        # enters x to exit the program. x is listed an option to exit.
        
        # I dont think there is a simpler way to meet spec vrequirement without creating this
        # code block as we need the menu to loop here and repeat as required.
        # What is the closest alternative to creating this code block?
        # The closest alternative to this condition that I could think
        # of is an example of spaghetti code, which would not be appropriate in this instance.
        # while True:
        #   if statements as normal
        #   if (choice == "x"):
        #           break
        
        # The statements kept inside  directly relate to the operations listed in
        # the menu.
        # The if statements will trigger an operation as listed in the menu options. 
        # If the user enters"x" in choice the UI will stop.
        
        while (choice!= "x"):
            
            # (Justification comment for condition below)
            # v is listed as an operation in the menu.
            # That will trigger this if statement.
            # I dont think there is a simpler way to write this code to meet
            # requirements.
            # Statemets within are listed in order to communicate and take
            # input from the user and carry out the operations as listed in the
            # menu options.
    
            if (choice== "v"):
                sys.stdout.write("\n"+"Accounts".center(40,"-"))
                sys.stdout.write("\n")
                sys.stdout.write(self.__backend.display_accounts())
                
            # (Justification comment for condition below)   
            # a is listed as an operation in the menu.
            # That will trigger this if statement.
            # I dont think there is a simpler way to write this code to meet
            # requirements.
            # Statemets within are listed in order to communicate and take
            # input from the user and carry out the operations as listed in the
            # menu options.
            
            elif (choice== "a"):
                sys.stdout.write("\n"+"Add new account".center(40,"-"))
                sys.stdout.write("\n\n")
                
                # (Justification comment for variable below)
                # Alternative names I could have used are new_acc_num or
                # number, however new_account_number was more suitable to
                # represent the context saved in the variable. 
                # get_int is required as the account numbers are stored as
                # INT which is consistant with other banks.
                
                new_account_number = FrontEnd.__get_positive_int("Enter new account number (4-10 digits): ")

                # (Justification comment for variable below)
                # Alternative names I could have used are new_acc_name or
                # name, however new_account_name was more suitable to
                # represent the context saved in the variable.
                # get_str is required on this input to ensure the data is
                # stored as string consistant throughout the program.
                # There is no real need on the backend for a string data
                # type however it would make the account easier for the
                # customer to recognise by putting a name to it.
                
                new_account_name = FrontEnd.__get_str("Enter new account name (4-10 digits): ")

                # (Justification comment for variable below)
                # Alternative names I could have used are opening_balance
                # or money, however new_account_balance was more suitable
                # to represent the context saved in the variable.
                # get_float is required as the account balances are stored
                # as float to allow addition and subtraction to decimal
                # values such as normal money transactions which is consistant
                # with other banks.
                
                new_account_balance = FrontEnd.__get_positive_float("Balance: ")
                
                # (Justification comment for code block below Try and Except)
                # Built in errors can be raised from running this operation
                # and stop the program, I chose to use a try and except here
                # to avoid this issue. If a new object cannot be created it
                # will not break the program.
                
                # As I have already included functions to validate the user
                # input of type before it is sent to the backend, the errors
                # raised will be due to the object creation rules which
                # specify min and max length on account name and account number.       
 
                try:
                    self.__backend.add_account(new_account_number,new_account_name, new_account_balance)
                    sys.stdout.write("Account created successfully.\n")
                except:
                    sys.stderr.write("Problem, account number and name must be at least 4-10 digits.")
            
            # (Justification comment for code block below)
            # s is listed as an operation in the menu.
            # That will trigger this if statement.
            # I dont think there is a simpler way to write this code to meet
            # requirements.
            # Statemets within are listed in order to communicate and take
            # input from the user and carry out the operations as listed in the
            # menu options.
            
            elif (choice== "s"):
                
                # (Justification comment for variable below)
                # Alternative names I could have used are file_name or f
                # however I thought this was sufficient for this purposes
                # and describes its purpose and the context of the data
                # saved to the variable.
                
                file_name = FrontEnd.__get_str("\nEnter file name: ")

                # (Justification comment for code block below try and except)
                # Built in errors can be raised from running this operation
                # and stop the program, I chose to use a try and except
                # here to avoid this issue and handle the exception.
                # If the file named cannot be saved such as if the
                # status is read-only the export_data function will break
                # the program.
                
                try:
                    self.__backend.export_data(file_name)
                except:
                    sys.stderr.write("Error: Could not export file. Check the file name and try again.")      

            # (Justification comment for condition below)
            # d is listed as an operation in the menu.
            # That will trigger this if statement.
            # I dont think there is a simpler way to write this code to meet
            # requirements.
            # Statemets within are listed in order to communicate and take
            # input from the user and carry out the operations as listed in the
            # menu options.
            
            elif (choice=="d"):
                
                # (Justification comment for variable below)
                # Alternative names I could have used are acc_num or number,
                # however account_number was more suitable to represent
                # the context saved in the variable. get_positve_int
                # is required as the account numbers are stored as
                # INT which is consistant with other banks.
                # Alternatively, the account number could have been
                # represented as string however, that would make it
                # difficult to keep the account ID consistant and seperate
                # from the name.
                
                account_number = FrontEnd.__get_positive_int("Enter account number: ")

                # (Justification comment for variable below)
                # Alternative names I could have used are acc_name or name,
                # however account_name was more suitable to represent the
                # context saved in the variable.
                # get_str is required on this input to ensure the data is
                # stored as string consistant throughout the program.
                # There is no real need on the backend for a string
                # data type however it would make the account easier for the
                # customer to recognise by putting a name to it.
                
                account_name =FrontEnd.__get_str("Enter account name: ")
                
                # (Justification comment for variable below)
                # Alternative names I could have used are deposit or money,
                # however deposit_amount was more suitable to represent
                # the context saved in the variable.
                # __get_positive_float is required as the account balances
                # are stored as float to allow addition and subtraction
                # to decimal values such as normal money transactions
                # which is consistant with other banks.
                
                deposit_amount=FrontEnd.__get_positive_float("Enter deposit amount:")

                # (Justification comment for condition below IF and ELSE)
                # I have inlcuded if and else statements to confirm if the
                # transaction was successful or not to the customer.
                # This is not stated in the requirements but I like to at confirm
                # if the operation is successful or not to the user to improve the
                # user experience.

                if(self.__backend.deposit(account_number, account_name, deposit_amount)==True):
                    sys.stdout.write("\nTransaction successful")
                else:
                    sys.stdout.write("Problem, the account details could not be found.")

            # (Justification comment for condition below)
            # w is listed as an operation in the menu.
            # That will trigger this if statement.
            # I dont think there is a simpler way to write this code to meet
            # requirements.
            # Statemets within are listed in order to communicate and take
            # input from the user and carry out the operations as listed in the
            # menu options.
            elif (choice=="w"):
                sys.stdout.write("\n")
                
                # (Justification comment for variable below)
                # Alternative names I could have used are acc_num or number,
                # however account_number was more suitable to represent
                # the context saved in the variable. get_int is required
                # as the account numbers are stored as INT which is
                # consistant with other banks.
                
                account_number =FrontEnd.__get_positive_int("Enter account number: ")

                # (Justification comment for variable below)
                # Alternative names I could have used are acc_name
                # or name, however account_name was more suitable
                # to represent the context saved in the variable.
                # get_str is required on this input to ensure the
                # data is stored as string consistant throughout
                # the program. There is no real need on the backend
                # for a string data type however it would make the
                # account easier for the customer to recognise
                # by putting a name to it.
                
                account_name = FrontEnd.__get_str("Enter account name: ")
                
                # (Justification comment for variable below)
                # Alternative names I could have used are withdrawal
                # or money, however
                # withdrawal_amount was more suitable to represent the
                # context saved in the variable.
                # __get_positive_float is required as the account
                # balances are stored as float to allow addition
                # and subtraction to decimal values such as normal
                # money transactions which is consistant with other
                # banks.
                
                withdrawal_amount=FrontEnd.__get_positive_float("Enter withdrawal amount:")

                # (Justification comment for code block below try and except)
                # Built in errors can be raised from running this operation
                # and stop the program, I chose to use a try and except here
                # to avoid this issue and handle the exception.
                
                # If the balance is less than the withdrawal amount it would
                # raise the zerodivisionerror, and this try/except will
                # continue the program without breaking.
                
                try:
                    # (Justification comment for code block below if/else)
                    # The backend class method will return a boolean to confirm if
                    # the operation requested has completed successfully or failed.
                    # If true/false then then a message to confirm status
                    # will print on the screen to the user. 

                    if (self.__backend.withdrawal(account_number, account_name, withdrawal_amount)==True):
                        sys.stdout.write("\nTransaction successful\n")
                    else:
                        sys.stdout.write("Problem, the account details could not be found.")
                except:
                    sys.stderr.write("Problem, not enough funds to perform this transaction.")

            # (Justification comment for condition below)
            # Choice options is listed as an operation in the menu, if an option was
            # entered that is not included in the menu else will confirm the
            # option is invalid to the user. 
            # I dont think there is a simpler way to write this code to meet
            # requirements.
            # Statemets within are listed in order to communicate and take
            # input from the user and carry out the operations as listed in the
            # menu options.
            
            else:
                sys.stdout.write("Choice not valid: \n")
                
            # (Justification comment for variable below)
            # Alternative names I could have used are options, user_input, however
            # for consistancy I chose to keep choice as it describes the user choice
            # of input. get_str is called in this variable as to ensure the input is
            # not blank and break the program.  
            choice = FrontEnd.__get_str(menu).lower()
        self.__backend.save_data()

    # (Justification comment for code block below)
    # the purpose of this function is to initialize the string data input from
    # the user in order to keep the program running without error from blank
    # user input. I'm not sure if there are alternatives to this function.

    # The reason for this function is to continuously prompt the user
    # for the correct data type at the time of requesting input
    # and also to reduce the amount of code required as input
    # and prompt is combined within this function. 

    def __get_str(prompt:str)->str:
        sys.stdout.write(prompt)
        return sys.stdin.readline().strip()

    # (Justification comment for code block below)
    # the purpose of this function is to initialize the float type data input
    # from the user in order to keep the program running without error from
    # blank user input. I'm not sure if there are alternatives to this function.

    # The reason for this function is to continuously prompt the user
    # for the correct data type at the time of requesting input
    # and also to reduce the amount of code required as input
    # and prompt is combined within this function.

    # opting to use get_positive_int as its function rather than using get_str is to
    # avoid getting input errors as using __get_str(int(prompt)) is all well and
    # fine but converting a string to int when a letter is input will raise an
    # error and to get around this.
    # this function was used to:
    #   1) check the value of the input is int
    #   2) check that the value is a positive number
    
    def __get_positive_int(prompt:str)->str:
        
        # (Justification comment for variable)
        # while the value is None the function will repeatedly prompt
        # the user for input and check the input is a positive value.
        # This is neccessary to validate the user input and avoid errors
        # raised from the backend by sending incorrect data types to it.
        
        value = None
        
        # (Justification comment for code block below)
        # while the value is equal to None means the input recieved has
        # no value such as a letter and this while loop will run until
        # the value is not equal none. The purpose is to have the
        # conditions in the while loop to check and prompt
        # the user repeatedly to enter the correct data type.
        # Alternatively I could have written the condition as
        # while value is not >= 0

        while (value == None):
            
            # (Justification comment for code block below)
            # try is used to avoid error from converting string to int
            # in the event of the user entering a letter in the input
            # request. If it does not meet the requirement, the except will
            # be triggered to prompt for input until an answer is provided that
            # meets the conditions.

            try:
                # (Justification comment for variable below)
                # When the input is recieved the value should be float as in
                # the value should not be equal to none, the function will
                # repeatedly prompt the user for input and check the input
                # is a positive value.
                # This is neccessary to validate the user input and avoid errors
                # raised from the backend by sending incorrect data types to it.
                
                value = int(FrontEnd.__get_str(prompt))

                # (Justification comment for code block below)
                # while the value is less than 0 it means the input recieved 
                # has no value or is negative and this while loop will run until
                # the value is not equal to none and is positive.
                # The purpose is to have the conditions in the while
                # loop to check and prompt the user repeatedly to enter
                # the correct data type.
                # Alternatively I could have written the condition as
                # while value is not >= 0 

                while ( value < 0 ):
                    
                    # (Justification comment for code block below)
                    # try is used to avoid error from converting string to int
                    # in the event of the user entering a letter in the input
                    # request. If it does not meet the requirement, the except will
                    # be triggered to prompt for input until an answer is provided that
                    # meets the conditions.
                   
                    try:
                        # (Justification comment for variable below)
                        # When the input is recieved the value should be int as in
                        # the value should not be equal to none, the function will
                        # repeatedly prompt the user for input and check the input
                        # is a positive value.
                        # This is neccessary to validate the user input and avoid errors
                        # raised from the backend by sending incorrect data types to it.
                        value = int(FrontEnd.__get_str(prompt))
                    
                    # (Justification comment for code block below)
                    # if the user input recieved does not meet the conditions set in the try
                    # code block it will trigger this exception to prompt the user
                    # to re-enter repeatedly until the correct input is entered. 
                    
                    except:
                        prompt="Problem, that wasn't right. Re-enter a positive number: "
            
            # (Justification comment for code block below)
            # if the user input recieved does not meet the conditions set in the try
            # code block it will trigger this exception to prompt the user
            # to re-enter repeatedly until the correct input is entered.
            
            except:
                prompt="Problem, that wasn't right. Re-enter a positive number: "
        return value   
    
    # (Justification comment for code block below) 
    # the purpose of this function is to initialize the float type data as a
    # positive float input from the user in order to keep the program running
    # without error from blank user input. 
    # The reason I have __get_foat and __get_positive_float is as a result of
    # the testing, if a letter was entered by the user,
    # the program would break as it cannot convert string to float.
    # My theory is that I create 2 functions to initialize float input
    # but _get_float just checks for the correct data type and
    # get_positive_float checks that the float input is actually positive.
    # I'm not sure if there are alternatives to this function.

    def __get_positive_float(prompt:str)->str:
        
        # (Justification comment for variable below)
        # while the value is None the function will repeatedly prompt
        # the user for input and check the input is a positive value.
        # This is neccessary to validate the user input and avoid errors
        # raised from the backend by sending incorrect data types to it.
        
        value = None
        
        # (Justification comment for code block below)
        # while the value is equal to None means the input recieved has
        # no value such as a letter and this while loop will run until
        # the value is not equal none. The purpose is to have the
        # conditions in the while loop to check and prompt
        # the user repeatedly to enter the correct data type.
        # Alternatively I could have written the condition as
        # while value is not >= 0

        while (value==None):
            
            # (Justification comment for code block below try)
            # try is used to avoid error from converting string to int
            # in the event of the user entering a letter in the input
            # request. If it does not meet the requirement, the except will
            # be triggered to prompt for input until an answer is provided that
            # meets the conditions.
            
            try:
                # (Justification comment for variable below)
                # When the input is recieved the value should be float as in
                # the value should not be equal to none, the function will
                # repeatedly prompt the user for input and check the input
                # is a positive value.
                # This is neccessary to validate the user input and avoid errors
                # raised from the backend by sending incorrect data types to it.
                
                value=float(FrontEnd.__get_str(prompt))
                
                # (Justification comment for code block below)
                # while the value is less than 0 it means the input recieved 
                # has no value or is negative and this while loop will run until
                # the value is not equal to none and is positive.
                # The purpose is to have the conditions in the while
                # loop to check and prompt the user repeatedly to enter
                # the correct data type.
                # Alternatively I could have written the condition as
                # while value is not >= 0 but due to the errors raised in testing
                # I couldn't get the alternative to work properly. 
              
                while (value<0):
                    
                    # (Justification comment for code block below try)
                    # try is used to avoid error from converting string to float
                    # in the event of the user entering a letter in the input
                    # request. If it does not meet the requirement, the except will
                    # be triggered to prompt for input until an answer is provided that
                    # meets the conditions.
                    
                    try:
                        # (Justification comment for variable below)
                        # When the input is recieved the value should be float as in
                        # the value should not be equal to none, the function will
                        # repeatedly prompt the user for input and check the input
                        # is a positive value.
                        # This is neccessary to validate the user input and avoid errors
                        # raised from the backend by sending incorrect data types to it.
                        
                        value=float(FrontEnd.__get_str(prompt))

                    # (Justification comment for code block below)
                    # if the user input recieved does not meet the conditions set in the try
                    # code block it will trigger this exception to prompt the user
                    # to re-enter repeatedly until the correct input is entered. 
                   
                    except:
                        prompt="Problem, that wasn't right. Re-enter a positive number: "

            # (Justification comment for code block below)
            # if the user input recieved does not meet the conditions set in the try
            # code block it will trigger this exception to prompt the user
            # to re-enter repeatedly until the correct input is entered. 
    
            except:
                prompt="Problem, that wasn't right. Re-enter a positive number: "             
        return value
            
    





        



    
        
        
        
