# (Justification comment for code block below)
# Previously my bank accounts application records stored in separate lists
# without classes.
# In comparing the two blocks of codes, I believe that the class IS the more
# simplest alternative as all of the data is stored in one record. Relying on
# separate lists just seems untrustworthy, as it would be complex to control
# with mutliple pieces of data. I also think setting the limitations of each
# detail of the record is simpler as once the lists are out of
# sync it would be difficult to control. At least with the class we can set
# as much limitations and checking while also keeping the records together
# in one spot.

# The closest alternative to creating this code block with a class and constructor to
# initalize would be to just have a function to check and append data to seperate
# lists as we have different data types in this class.
# Placing limitations on the data created and appended would be alot more
# complex to validate each piece of data.
# an example of the alternative as a function could be the following
# def add_data(number, name, balance):
#       confimed_record = None
#       details_valid = 0
#       while confirmed == None:
#           if (number >= 0):
#                details_valid += 1
#           if (len(name) >= 4):
#               details_valid += 1
#           if (balance >= 0):
#               details_valid += 1
#       if (details_valid ==3):
#           bank_numbers.append(number)
#           bank_names.append(name)
#           bank_balances.append(balance)

# the statements in this class directly relate to the creation of the class
# objects and the rules set on each attribute. I believe that this is in
# keeping with the Object Oriented Programming foundation principles of
# encapsulation to keep the data of this class private and managed
# within the class.

# The statements are each grouped in order by how the records are created/listed.

# 1 Account number
# 2 Account name 
# 3 Account balance

# The constructor is set in this order as well as the accessor and mutators.
# I left the order as this for readability as well as the fact the constructor
# should be listed first its the most logical thing to if that is the function to
# initialize each instance of this class. The accessors are second as the mutators
# cannot be called unless there is an accessor declared first. Normally the code
# is read top to bottom inside functions but I can't be sure about class members,
# however if function present I suppose it will just read when it is called.

class BankAccounts:
    
    # (Justification comment for code block below)
    # I'm not sure if there is a simpler way to meet the requirements without
    # creating this code block or if there is an alternative to init due to the
    # fact that Init is a built in function within Python that is used to
    # initialize new instances of an object created of that class.
    # The oxford dictionary defines Initialize as set to the value or put in the
    # condition appropriate to the start of an operation. The definition describes
    # exactly what is going on in the Init function.

    # The closest alternative to this code block would be just to create a
    # function to recieve the arguements and validate before sending to the backend,
    # but if I were to do that, it would not follow the OOP encaspulation guidelines.
    
    # Init includes declares the class attributes that should be applied to each
    # object created from this class is listed
    # in init in order to initialize the records.

    # The statements are each grouped in order by how the records are
    # created/listed.

    # 1 Account number
    # 2 Account name 
    # 3 Account balance
    
    def __init__(self, account_number:int, account_name:str, account_balance:float):

        #(Justification for variable and data type below)
        # A suitable alternative name for this variable could be
        # acc_number or number.

        # I believe the name I have chosen more appropriate as the name is an accurate
        # description of the data saved to this variable and in order to keep the program
        # naming conventions consistant and also consise for debugging and reading.
    
        # Another programmer can argue that string data type would be perfectly
        # fine as we are not using this variable to do any mathematic calculations.
    
        # That is correct, however bank account ID numbers are historically a string
        # of multiple ID numbers such BSB and Account number.
        # BSB represents the location of the branch like a post code.
        # The account number is normally generated in order of accounts by bank.
        # Keeping all this mind, using INT to keep the input strictly as numerical digits,
        # will keep the application inline with that guideline.
        
        self.account_number = account_number
        
        #(Justification for variable and data type below)
        # Alternatively, I could have called it name, acc_name or similiar
        # however I didnt think they would be as suitable for this program as
        # I wanted to keep the code clear and easy to read.
    
        # I think the name I have chosen is more appropriate or not worse because account_name
        # is consistant throughout the program and other banks.

        # Data type is string in order to let the user create their own descriptive or
        # unique name for the account.
        
        self.account_name = account_name
        
        #(Justification for variable and data type below)
        # Alternatively, I could have called it balance, acc_bal or similiar
        # however I didnt think they would be as suitable for this program as
        # I wanted to keep the code clear and easy to read.
        
        # This variable name account_balance is consistant throughout the
        # program and other banks and therefor more appriopriate or not worse
        # than the alternatives.
        
        # I chose to use float as the data type for this variable as shown in
        # the setter or mutator.
        # Float allows us to use decimal similar to money and also carry
        # out addition and subtraction on the values to represent the
        # transactions submitted by the user in the frontend. 
        self.account_balance = account_balance

    # (Justification comment for code block below)
    # I dont think there is a simpler way to meet the requirements of the spec
    # without creating this code block.
    
    # In order to keep the attribute private we have to create an accessor
    # to access the attributes outside of this class in the application.
    
    # As there is only a return  statement, when this method is called, it
    # will return the property as called.
    
    # As this is an accessor and decorated with the @property the hidden
    # attribute can be
    # accessed outside of the class. It is not neccessary to include any
    # other code in this code block.
    @property
    def account_number(self)->int:
        return self.__account_number
    
    # (Justification comment for code block below)
    # decorator used as this function will return the property called within.
    
    # I dont think there is a simpler way to meet the requirements of the spec
    # without creating this code block.
    # In order to keep the attribute private we have to create an accessor
    # to access the attributes in the application.
    
    # As there is only a return  statement, when this method is called, it
    # will return the property as called.
    
    # As this is an accessor and decorated with the @property the hidden
    # attribute can be
    # accessed outside of the class. It is not neccessary to include any
    # other code in this code block.
    @property
    def account_name(self)->str:
        return self.__account_name
    
    # (Justification comment for code block below)
    # I dont think there is a simpler way to meet the requirements of the spec
    # without creating this code block.
    # In order to keep the attribute private we have to create an accessor
    # to access the attributes in the application.
    
    # As there is only a return  statement, when this method is called, it
    # will return the property as called.
    
    # As this is an accessor and decorated with the @property the hidden
    # attribute can be
    # accessed outside of the class. It is not neccessary to include any
    # other code in this code block.
    
    @property
    def account_balance(self)->float:
        return self.__account_balance
    
    # (Justification comment for code block below)
    # In order to control the objects created from this class, it was neccessary to
    # include rules to ensure that the length is within the specified length and
    # of the correct data type. If the input does not meet these requirements
    # the object will not be created.
    # The reason for the length is to keep consistancy in the records created.

    # It could be argued that the alternative to creating this code is to ensure
    # the input is validation in the frontend is more stringent,
    # however in keeping with the OOP principle of encapsulation by ensuring
    # this class takes care of itself, this code is neccessary.

    # The setter decorator was used as this function will set the property on an object within
    # the specified limitations set.
    # Why are these statements in this order? What haven’t you added into the code block and why?
    # To set the atribute should not meet both conditions set on the if
    # statements included.
    # The reason I set both as if and not if/elif is to have both checked
    # and not just one. If the input does meet the conditions an error will
    # not be raised and the value will be set.
    
    # The order is set to read from top to bottom:
    #           1) Is the input value less than 4 digits, if yes raise
    #              the value error and do not go any further,if no move the
    #              next step.
    #           2) Is the input value equal or more than 10 digits, if yes
    #              raise the value error and do not go any further, if no move
    #              to the next step.
    #           3) set the value on the object.
    
    @account_number.setter
    def account_number(self, value:int):
        
        if (len(str(value))< 4):
            raise ValueError ("Account number must be at least 4 digits.")
        
        if (len(str(value))>= 10):
            raise ValueError ("Account number must be equal or less than 10 digits.")
        self.__account_number = value
        
    # (Justification comment for code block below)
    # In order to control the objects created from this class, it was neccessary to
    # include rules to ensure that the length is within the specified length and
    # of the correct data type. If the input does not meet these requirements
    # the object will not be created.
    # The reason for the length is to keep consistancy in the records created.
    
    # It could be argued that the alternative to creating this code is to ensure
    # the input is validation in the frontend is more stringent,
    # however in keeping with the OOP principle of encapsulation by ensuring
    # this class takes care of itself, this code is neccessary.
    
    # The setter decorator was used as this function will set the property
    # on an object within the specified limitations set.

    # To set the atribute should not meet both conditions set on the if
    # statements included.
    # The reason I set both as if and not if/elif is to have both checked
    # and not just one. If the input does meet the conditions an error will
    # not be raised and the value will be set.
    
    # The order is set to read from top to bottom:
    #           1) Is the input value less than 4 digits(string), if yes raise
    #              the value error and do not go any further,if no move the
    #              next step.
    #           2) Is the input value equal or more than 10 digits(string), if yes
    #              raise the value error and do not go any further, if no move
    #              to the next step.
    #           3) set the value on the object.
    
    @account_name.setter
    def account_name(self, value:str):
        name_strip=value.strip()
        # (Justification comment for code block below)
        if (len(value)< 4):
            raise ValueError("Account name must be at least 4 digits.")
        # (Justification comment for code block below)
        if (len(value)>= 10):
            raise ValueError("Account name must be equal or less than 10 digits.")
        self.__account_name = value
        
    # (Justification comment for code block below)
    # In order to control the objects created from this class, it was neccessary to
    # include rules to ensure that input value is of the correct data type.
    # If the input does not meet this requirement the object will not be created.
    # Even though there is input validation in the front end to prevent negative
    # float to be sent to the backend. This will also stop the file data loaded
    # into the program with negative balances as the program would not work as
    # intended, if this any negative balances.

    # It could be argued that the alternative to creating this code is to ensure
    # the input is validation in the frontend is more stringent,
    # however in keeping with the OOP principle of encapsulation by ensuring
    # this class takes care of itself, this code is neccessary.

    # The setter decorator was used as this function will set the property on
    # an object within the specified limitations set.
    
    # To set the atribute should not meet the if condition set on the statement
    # included.
    #
    # The order is set to read from top to bottom:
    #           1) Is the input value is less than 0, if yes raise
    #              the value error and do not go any further,if no move the
    #              next step.
    #           2) set the value on the object.
    
    @account_balance.setter
    def account_balance(self, value:float):

        # (Justification comment for code block below)
        # In order to ensure that this class follows the OOP principle of encapsulation,
        # it is neccessary to include this to avoid issues in the program if a
        # negative value was used for an account balance,
        # hence this if statement was included to validate the account balance is not
        # negative before setting the attribute.
        
        # The alternative is to not inlcude this condition and leave the frontend
        # to validate with the get_positive_float function however as I have
        # stated previously this is neccessary to ensure the class looks after itelf.
        # The error raised will let other developers know what the issue is if
        # there is a problem.
        
        if value < 0 :
            raise ValueError ("Account Balance cannot be negative")
        self.__account_balance = value

# -------------------------------------------------------------------------   
# (Justification comment for code block below)
# Backend class created to manage the BankAccount class and send
# information to the FrontEnd class.
# It could be argued that there is a simpler way to creating a backend class to
# manager the objects from BankAccounts and send it to the frontend class.
# But I believe that this is inline with the model controller where the
# frontend does not directly talk to the class which creates the object,
# but a separate class that manages the objects.

# I'm not sure that there is an alternative to creating a class, we could just
# create functions as shown in my last major assignment but the class structure
# seems to be more appropriate in grouping all the methods and functions.
# Creating objects from this group means we can re-use the code later.

# This class includes a contructor to hold a file_name to import and export
# data and a list to save new objects created from the BankAccounts class,
# aswell as series of methods or functions to communicate to the frontend and
# read/write to csv file. 

class BackEnd:
    
    # (Justification comment for code block below)
    # A constructor is required in the spec in each class.
    # I dont think there is a simpler way to meet the requirements other than
    # what I have included in this init.

    # The closest alternative could just be a function within the class to
    # set the attributes.
    
    # The parameters is set to recieve self and file_name, so the file name is required
    # when creating this object and calling it.
    
    def __init__(self, file_name:str):

        # (Justification comment for variable below)
        # file_name used to accurately represent the
        # data passed from app.py. Alternatively, I could have used x or file
        # however I chose to keep the naming conventions consistant for easy reading.
        self.__file_name=file_name

        #(Justification for variable and data type below)
        # Alternatively, I could have used bank_user_list or bank_records.
        # I used bank_accounts as this list name, I thought this would be suitable
        # as it represents the context saved to the list.
        self.__bank_accounts = []

    # (Justification comment for code block below)
    # Function created to load data from an existing file external to the
    # program and append the data into the lists of the program.
    # It made sense to create its own function to perform this action to
    # easily maintain the code.
    # load_data accurately represents the operation in this function.

    def load_data(self):
        # (Justification comment for code block below)
        # try and except used due to errors that can be raised during the load
        # file process.
        # As there are limitations placed on the BankAccount objects, it could
        # break the program. It can also break from file_name error such as
        # file not found.
        try:
            # (Justification comment for variable below)
            # file_object named to keep consistancy, alternatively
            # I could have called it file or file_obj.
            file_object = open (self.__file_name, "r")
            
            # (Justification for variable and data type below)
            # line variable to called readline on the file_object. Alternatively,
            # I could have called is read_file_line or similiar however,
            # I chose to keep it simple with line to represent the action.
            line = file_object.readline().strip()
            
            # (Justification comment for condition below)
            # while lines is not blank the loop will continue to read the data on
            # the file and append the details found in the lists.
            
            # Alternatively I could have used the example found in wk 6 Expense manager,
            # as follows:
            #   with open("expenses.csv", "r") as file_object:
            #               for line in file_object:
            # However, I chose to use the condition below as that is within the spec of
            # this assignment.
            while (line != ""):
                fields = line.split(",")
                
                #(Justification for variable and data type below)
                # account_number is consistant with BankAccounts class attribute
                # which is represented in column 1 of the csv file.
                # The data type of that attribute is INT therefor this field
                # will append to that class below as that type.
                account_number = int(fields[0])
                
                #(Justification for variable and data type below)
                # account_name to represent the BankAccount property from column
                # 2 in the csv file, the data type of that class attrbiute is string.
                account_name = fields[1]
                
                #(Justification for variable and data type below)
                # account_balance to represent the BankAccount property from
                # column 3 of the csv file, the data type of that class
                # attribute is float.
                account_balance = float(fields[2])
                self.add_account(account_number, account_name, account_balance)
                
                # (Justification for variable and data type below)
                # line variable to called readline on the file_object. Alternatively,
                # I could have called is read_file_line or similiar however,
                # I chose to keep it simple with line to represent the action.
                line = file_object.readline().strip()
            file_object.close()
            
        # (Justification comment for code block below)
        # I dont think there is a simpler way to meet the spec requirements
        # without creating this code block as it is stated that it is a
        # requirement to raise inbuilt exceptions and handle them in the frontend.
        
        # In the event of an error with the try code block above with the file,
        # it will trigger this except block and and raise an exception.
    
        except:
            raise FileNotFoundError ("File cannot be found")
        
    # (Justification comment for code block below)
    # Function created to add new account details to the list and create new
    # BankAccount objects.
    # add_account was suitable as the name in this instance as it describes the
    # operation of the function.
    # Alternatively, I could have written the code differently to appended by saving
    # the object to a new variable and then append with the next line. 
    # but this was more efficient. 
    def add_account(self, account_number:int, account_name:str, account_balance:float):
        self.__bank_accounts.append(BankAccounts(account_number, account_name, account_balance))
        
    # (Justification comment for code block below)
    # The purpose of this function is to recieve the input from the user in the
    # front end and find a match to those details. The value is then amended as
    # per the deposit amount.
    # The alternative to this method would be to just use 1 parameter
    # to find a matching record and therefor simplify the loop but I was thinking more in terms
    # of the fact, I didnt have the time to investigate creating a rule to check if a
    # duplicate record has been created in the class. If there were no duplicates
    # it wouldnt need 2 records to find a match.
    def deposit(self, account_number:int, account_name:str, deposit_amount:float)->bool:
        
        #(Justification for variable and data type below)
        # deposit_result variable will store a boolean to return to the
        # frontend, this will confirm to the user if the deposit operation was
        # successful or not. The main reason it would not be successful is if
        # the bank account and bank name user input did not match what is
        # currently existing in the program. Alternative names I could have used a
        # number or letter to represent this but boolean seemed to make more sense.
        deposit_result = None
        
        #(Justification for variable and data type below)
        # Alternative names I could have used is matches, or total_matches
        # but I thought matching_parameters was more suitable due to the
        # description is easier to see what this means in the while loop.
        # matching_parameters is a variable to store thetotal matches found
        # in iteration of the list in the while loop below, comparing the
        # parameters passed to the backend from the frontend against
        # current class objects.
        matching_parameters = 0

        #(Justification for variable and data type below)
        # Alternatively, I could have named it num_accounts or x, however this
        # seemed sufficient in this instance.   
        # variable created to represent the length or items found within the
        # accounts list.
        # Data type is int to find the length of bank_accounts list.
        len_self_accounts=len(self.__bank_accounts)
        
        #(Justification for variable and data type below)
        # index named as the variable to reflect that it is running through
        # each index of the list.
        # Alternatively, I could have used x, or i, however this was sufficient.
        # data type is int, as it will allow increment added at the end of each
        # run.
        
        # The data type is int, I dont think there is a more suitable data-type
        # for the value stored in this
        # variable as it is required to increment by 1 with the each item
        # in the list called.
        index = 0
        
        # (Justification comment for condition below)
        # I believe it is possible to use a for loop in this instance however,
        # I chose to use this condition as it is within the spec of this
        # assignment.
        # It is sufficient to only have the loop run the length of the items
        # within the lists, to find a match. Matching parameters have also been
        # included so we can find 2 matches of the same index.
        while (index<len_self_accounts and matching_parameters <2):
            
            #(Justification for variable and data type below)
            # Alternative names I could have used is matches, or total_matches
            # but I thought matching_parameters was more suitable due to the
            # description is easier to see what this means in the while loop.
            # matching_parameters is a variable to store thetotal matches found
            # in iteration of the list in the while loop below, comparing the
            # parameters passed to the backend from the frontend against
            # current class objects.
            matching_parameters=0
            
            # (Justification comment for condition below)
            # If class object account number is equal to the user input saved to
            # account number then add 1 to matching_parameters.
            # Once the loop has run through both records at this index it
            # reset the matching parameters and will move on to the next index.
            if self.__bank_accounts[index].account_number == account_number:
                matching_parameters+=1
            # (Justification comment for condition below)
            # If class object account name is equal to the user input saved to
            # account name then add 1 to matching_parameters.
            # Once the loop has run through both records at this index it
            # reset the matching parameters and will move on to the next index.
            if self.__bank_accounts[index].account_name == account_name:
                matching_parameters+=1
            # (Justification comment for condition below)
            # As the code is read top to bottom if there no matches against
            # the user input in the previous if statements then the loop
            # will continue and add +1 to the index to move on the next position
            # in the list to check. 
            if (matching_parameters<2):
                index+=1
        # (Justification comment for condition below)
        # if the loop ends with matching parameters greater than or equal to 2,
        # it will trigger this if statement and update the account balance as
        # per the deposit amount.
        if (matching_parameters>=2):
            self.__bank_accounts[index].account_balance += deposit_amount
            #(Justification for variable and data type below)
            # deposit_result variable will store a boolean to return to the
            # frontend, this will confirm to the user if the deposit operation was
            # successful or not. The main reason it would not be successful is if
            # the bank account and bank name user input did not match what is
            # currently existing in the program. Alternative names I could have used a
            # number or letter to represent this but boolean seemed to make more sense.
            deposit_result = True
        else:
            #(Justification for variable and data type below)
            # deposit_result variable will store a boolean to return to the
            # frontend, this will confirm to the user if the deposit operation was
            # successful or not. The main reason it would not be successful is if
            # the bank account and bank name user input did not match what is
            # currently existing in the program. Alternative names I could have used a
            # number or letter to represent this but boolean seemed to make more sense.
            deposit_result = False
        return deposit_result
    
    # (Justification comment for code block below)
    # The purpose of this function is to recieve the input from the user in the
    # front end and find a match to those details. The value is then amended as
    # per the deposit amount.The alternative to this method would be to just use 1 parameter
    # to find a matching record and therefor simplify the loop but I was thinking more in terms
    # of the fact, I didnt have the time to investigate creating a rule to check if a
    # duplicate record has been created in the class. If there were no duplicates
    # it wouldnt need 2 records to find a match.
    def withdrawal(self, account_number:int, account_name:str, withdrawal_amount:float)->bool:

        # (Justification for variable and data type below)
        # transaction_result variable will store a boolean to return to the
        # frontend, this will confirm to the user if the withdrawal operation was
        # successful or not. The main reason it would not be successful is if
        # the bank account and bank name user input did not match what is
        # currently existing in the program. Alternative names I could have used are
        # number (1) or letter(x) to represent this but boolean seemed to make more sense.
        transaction_result = False
        
        # (Justification for variable and data type below)
        # Alternative names I could have used is matches, or total_matches
        # but I thought matching_parameters was more suitable due to the
        # description is easier to see what this means in the while loop.
        # matching_parameters is a variable to store thetotal matches found
        # in iteration of the list in the while loop below, comparing the
        # parameters passed to the backend from the frontend against
        # current class objects.
        matching_parameters = 0

        #(Justification for variable and data type below)
        # Alternatively, I could have named it num_accounts or x, however this
        # seemed sufficient in this instance.   
        # variable created to represent the length or items found within the
        # accounts list.
        # Data type is int to find the length of bank_accounts list.
        
        len_self_accounts=len(self.__bank_accounts)
        
        #(Justification for variable and data type below)
        # index named as the variable to reflect that it is running through
        # each index of the list.
        # Alternatively, I could have used x, or i, however this was sufficient.
        # data type is int, as it will allow increment added at the end of each
        # run.
        
        # The data type is int, I dont think there is a more suitable data-type
        # for the value stored in this
        # variable as it is required to increment by 1 with the each item
        # in the list called.
        
        index = 0
        # (Justification comment for condition below)
        # I believe it is possible to use a for loop in this instance however,
        # I chose to use this condition as it is within the spec of this
        # assignment.
        # It is sufficient to only have the loop run the length of the items
        # within the lists, to find a match.
        while (index<len_self_accounts and matching_parameters <2):
            # (Justification comment for variable below)
            # matching_parameters is a variable to save the matches in the
            # while loop below, comparing the parameters passed to the
            # backend from the frontend against current class objects at each index.
            matching_parameters=0
            # (Justification comment for condition below)
            # If class object account number is equal to the user input saved to
            # account number then add 1 to matching_parameters.
            # Once the loop has run through both records at this index it
            # reset the matching parameters and will move on to the next index.
            if self.__bank_accounts[index].account_number == account_number:
                matching_parameters+=1
            # (Justification comment for condition below)
            # If class object account name is equal to the user input saved to
            # account name then add 1 to matching_parameters.
            # Once the loop has run through both records at this index it
            # reset the matching parameters and will move on to the next index.
            if self.__bank_accounts[index].account_name == account_name:
                matching_parameters+=1
            # (Justification comment for condition below)
            # As the code is read top to bottom if there no matches against
            # the user input in the previous if statements then the loop
            # will continue and add +1 to the index to move on the next position
            # in the list to check. 
            if (matching_parameters<2):
                index+=1
                
        # (Justification comment for condition below)
        # If the loop ends with matching parameters greater than or equal to 2,
        # it will trigger this if statement and update the account balance as
        # per the deposit amount.
        # I'm not sure if there is an alternative way to write this statement.
        if (matching_parameters>=2):   
                # (Justification comment for condition below)
                # if both matches are made, this if statement will trigger to do a
                # balance check by comparing withdrawal_amount to account balance. If the
                # account balance is greater than the withdrawal the action will be
                # performed. Else will raise the zerodivisionerror to be handled in
                # the frontend.
                # Alternatively, I could have written the if statement the opposite way around such as
                # if self.__bank_accounts[index].account_balance <= withdrawal_amount:
                #       raise ZeroDivisionError 
            if withdrawal_amount <= self.__bank_accounts[index].account_balance:
                # (Justification for variable and data type below)
                # transaction_result variable will store a boolean to return to the
                # frontend, this will confirm to the user if the withdrawal operation was
                # successful or not. The main reason it would not be successful is if
                # the bank account and bank name user input did not match what is
                # currently existing in the program. Alternative names I could have used are
                # number (1) or letter(x) to represent this but boolean seemed to make more sense.
                transaction_result = True
                self.__bank_accounts[index].account_balance -= withdrawal_amount
            else:
                raise ZeroDivisionError ("Cannot withdraw from zero")
            
        # (Justification comment for condition below)
        # If the loop ends with matching parameters less than 2,
        # it will trigger this else statement and update the transaction_result
        # boolean to False and that will be communicated to the frontend as a
        # failed operation request.
        # I'm not sure if there is an alternative way to write this statement.
        else:
            # (Justification for variable and data type below)
            # transaction_result variable will store a boolean to return to the
            # frontend, this will confirm to the user if the withdrawal operation was
            # successful or not. The main reason it would not be successful is if
            # the bank account and bank name user input did not match what is
            # currently existing in the program. Alternative names I could have used are
            # number (1) or letter(x) to represent this but boolean seemed to make more sense.
            transaction_result = False
        return transaction_result
    
    # (Justification comment for code block below)
    # The purpose of this function is to print the BankAccount objects created on
    # the screen to the user in the front end.
    # The closest alternative to this function is __str__ method where I can
    # print a simple list of strings of all of the objects from BankAccounts however,
    # I wanted to keep a running total of the ojects printed and chose to use this
    # method instead of __str__

    def display_accounts(self)->str:

        #(Justification for variable and data type below)
        # Alternatively, I could have named it num_accounts or x, however this
        # seemed sufficient in this instance.   
        # variable created to represent the length or items found within the
        # accounts list.
        # Data type is int to find the length of bank_accounts list.
        
        len_accounts = len(self.__bank_accounts)
        
        #(Justification for variable and data type below)
        # index named as the variable to reflect that it is running through
        # each index of the list.
        # Alternatively, I could have used x, or i, however this was sufficient.
        # data type is int, as it will allow increment added at the end of each
        # run.
        
        # The data type is int, I dont think there is a more suitable data-type
        # for the value stored in this
        # variable as it is required to increment by 1 with the each item
        # in the list called.
        
        index = 0
        
        # (Justification for variable and data type below)
        # total_amount is the variable created to save the total of all banks
        # listed to the user. I thought this was sufficient as it represents
        # the context of the data stored within, however I could have also
        # called it total_account_balances or similiar but I dont think that
        # level of detail was needed in this instance.

        total_amount=0
        
        # (Justification comment for variable below)
        # Alternative names I could have used are print_accounts
        # or display_accounts, but I thought this was sufficient
        # and chose to use view accounts and keep the code
        # consistant with the menu options.
        
        view_accounts = "\nAcc Number".ljust(15) + "Acc Name".ljust(15)
        view_accounts +="Balance".ljust(15)+"\n"
        
        # (Justification comment for condition below)
        # It made sense just to get the number of items currently within the
        # list so the loop will only run the necessary amount of times
        # required to fully perform the operation.
        # So if the len_accounts is greater than zero this code block.
        # We do not need this code block to run if there are no items in the lists.
        # I dont think there is a simpler way to write this code block.

        if len_accounts > 0:

            # (Justification comment for condition below)
            # It made sense just to get the number of items currently within the
            # list so the loop will only run the necessary amount of times
            # required to fully perform the operation.
            
            # While the index is less then the length of bank accounts list
            # the while loop will iterate through each index of the list by +1.
            # The details are then saved as a string to the view_accounts
            # variable.
            
            # The return statement will send the data to the frontend to print
            # on the screen to the user.
            
            while (index<len_accounts):
                view_accounts += f"{self.__bank_accounts[index].account_number:<15}" 
                view_accounts += f"{self.__bank_accounts[index].account_name:15}"
                view_accounts += f"{self.__bank_accounts[index].account_balance:>4.2f}"+"\n"
                total_amount+= self.__bank_accounts[index].account_balance
                index +=1
            view_accounts += "\n"+"Total Savings".rjust(30)+" $ "+ f"{total_amount:>4.2f}"
        return view_accounts

    # (Justification comment for code block below)
    # save_data created to write all of the bank account
    # details to csv.
    # This function uses the file_name recieved when
    # BackEnd is called in App.py

    def save_data(self):
        
        #(Justification for variable and data type below)
        # Alternative names I could have used are x, lines_to_write,
        # however in this instance I thoughts lines was sufficient
        # as its purposes is to just save data that will be written
        # in to the file. The name is a description of the contents
        # of the variable.
        lines = ""

        #(Justification for variable and data type below)
        # Alternatively, I could have named it num_accounts or x, however this
        # seemed sufficient in this instance.   
        # variable created to represent the length or items found within the
        # accounts list.
        # Data type is int to find the length of bank_accounts list.
        
        len_accounts=len(self.__bank_accounts)
        
        #(Justification for variable and data type below)
        # index named as the variable to reflect that it is running through
        # each index of the list.
        # Alternatively, I could have used x, or i, however this was sufficient.
        # data type is int, as it will allow increment added at the end of each
        # run.
        
        # The data type is int, I dont think there is a more suitable data-type
        # for the value stored in this
        # variable as it is required to increment by 1 with the each item
        # in the list called.
        
        index = 0
        
        # (Justification comment for condition below)
        # It made sense to get the number of items currently within the
        # list so the loop will only run the necessary amount of times
        # required to fully perform the operation.
        
        # export data is optional, I am sure it would have been much simpler to
        # allow the file_name attribute recieved in the constructor to be
        # changed but it doesnt seem appropriate to have a file name hard
        # coded in to app.py and then let the frontend override that by the
        # user because it would autosave upon closing.
        
        # While index is less than the length of bank accounts list, the details
        # of the bank accounts at that index will be saved to the lines variable.
        # Once the while has ended the file will open and the data saved to the
        # lines variable will be written to the file. The file is then closed.

        while(index<len_accounts):
            lines += str(self.__bank_accounts[index].account_number)+","
            lines += self.__bank_accounts[index].account_name+","
            lines += f'{self.__bank_accounts[index].account_balance:.2f}'+"\n"
            index +=1
        # (Justification comment for variable below)
        # file_object named to keep consistancy, alternatively
        # I could have called it file or file_obj.   
        file_object= open(self.__file_name,"w")
        file_object.write(lines + "\n")
        file_object.close()

    # (Justification comment for code block below)
    # I chose to create a seperate function to the save data as that function
    # uses the file_name saved to the class BackEnd and this function
    # will use the file_name input by the user in the frontend. It make sense
    # to have the frontend override the hardcoded file name to carry out the
    # auto load/save operation when the program opens and closes. 

    def export_data(self,file_name):

        #(Justification for variable and data type below)
        # Alternative names I could have used are x, lines_to_write,
        # however in this instance I thoughts lines was sufficient
        # as its purposes is to just save data that will be written
        # in to the file. The name is a description of the contents
        # of the variable.
        lines = ""

        #(Justification for variable and data type below)
        # Alternatively, I could have named it num_accounts or x, however this
        # seemed sufficient in this instance.   
        # variable created to represent the length or items found within the
        # accounts list.
        # Data type is int to find the length of bank_accounts list.

        len_accounts=len(self.__bank_accounts)
        
        #(Justification for variable and data type below)
        # index named as the variable to reflect that it is running through
        # each index of the list.
        # Alternatively, I could have used x, or i, however this was sufficient.
        # data type is int, as it will allow increment added at the end of each
        # run.
        
        # The data type is int, I dont think there is a more suitable data-type
        # for the value stored in this
        # variable as it is required to increment by 1 with the each item
        # in the list called.
        index = 0
        
        # (Justification comment for condition below)
        # It made sense to get the number of items currently within the
        # list so the loop will only run the necessary amount of times
        # required to fully perform the operation.
        
        # expert data is optional, I am sure it would have been much simpler to
        # allow the file_name attribute recieved in the constructor to be
        # changed but it doesnt seem appropriate to have a file name hard
        # coded in to app.py and then let the frontend override that by the
        # user because it would autosave upon closing.
        
        # While index is less than the length of bank accounts list, the details
        # of the bank accounts at that index will be saved to the lines variable.
        # Once the while has ended the file will open and the data saved to the
        # lines variable will be written to the file. The file is then closed.

        while(index<len_accounts):
            lines += str(self.__bank_accounts[index].account_number)+","
            lines += self.__bank_accounts[index].account_name+","
            lines += f'{self.__bank_accounts[index].account_balance:.2f}'+"\n"
            index +=1
        # (Justification comment for variable below)
        # file_object named to keep consistancy, alternatively
        # I could have called it file or file_obj.
        file_object= open(file_name,"w")
        file_object.write(lines + "\n")
        file_object.close()
        

            
        
        
        
    
        
