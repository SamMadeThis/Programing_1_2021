import sys
from car_modules import *

main_menu()
# justify variable name and datatype
# ---------------------------------------
# This variable will be used to save the user input and trigger the
# if-statements as per the menu options.
# Alternatively, I could have used input, user_input_options, x, a, etc,
# however, I thought user_input was sufficient in this instance.
# The datatype is string, I can also use INT as the menu is listed
# with numbers for the options, the result will be same. 
user_input = sys.stdin.readline().strip()
# justify variable name and datatype (line_break)
# ---------------------------------------
# decoration is a basic description of what the variable will be used
# for in the program.
# I could have used page_decoration, star_line, etc however, I thought
# decorate was short and sweet and to the point.
# The data type is string in order to print the text as needed. I could
# have used an INT and used 0's or something similar.
# I like the asterisk design and chose to go with string.
line_break="\n" + "-"*50 + "\n"
sys.stdout.write(line_break)

# justify the code block
# --------------------------------------
# Codes blocks will call the required function imported
# from another file as required in the specifications. 
# justify the condition
# --------------------------------------
# As the user_input variable will save a string, I have used the
# menu operation commands to trigger the if-statement blocks as required.
# I have used a while loop to keep the menu popping up automatically
# after each command has been entered by the user.
# Alternatively, I could have used INT on the user_input and achieve the same results.
while user_input != "5":
    # justify the code block (if & elif below)
    # --------------------------------------
    # Codes blocks will call the required function imported
    # from another file as required in the specifications. 
    # justify the condition (user_input == "1")
    # --------------------------------------
    # As the user_input variable will save a string,
    # I have used the menu operation commands to trigger
    # the if-statement blocks as required.
     if user_input == "1":
          all_cars()
          main_menu()
          user_input = sys.stdin.readline().strip()
          sys.stdout.write(line_break) 
     elif user_input == "2":
          werribee_cars()
          main_menu()
          user_input = sys.stdin.readline().strip()
          sys.stdout.write(line_break)             
     elif user_input == "3":
          sunburry_cars()
          main_menu()
          user_input = sys.stdin.readline().strip()
          sys.stdout.write(line_break)          
     elif user_input == "4":
          frankston_cars()
          main_menu()
          user_input = sys.stdin.readline().strip()
          sys.stdout.write(line_break)
        
sys.stdout.write("End program")

