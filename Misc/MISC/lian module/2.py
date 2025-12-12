import sys
from dealer_functions import all_car_models, werribee_models
from dealer_functions import sunbury_models, frankston_models

dashes ="=" * 80
welcome = "Welcome to Hyundai Australia!"
question = "What would you like to know?:\n"
question += "(A) Cars available at all dealers.\n"
question += "(B) Cars exclusive to Werribee.\n"
question += "(C) Cars exclusive to Sunbury. \n"
question += "(D) Cars exclusive to Frankston. \n"
question += "(E) Exit.\n"
question += "Your choice:"

sys.stdout.write(welcome.center(80, "="))
sys.stdout.write(question)
choice = sys.stdin.readline().upper().strip()
a = 0

while a == 0:
    if choice == "A":
        all_car_models()
        sys.stdout.write(question)
        choice = sys.stdin.readline().upper().strip()
    elif choice == "B":
        werribee_models()
        sys.stdout.write(question)
        choice = sys.stdin.readline().upper().strip()
    elif choice == "C":
        sunbury_models()
        sys.stdout.write(question)
        choice = sys.stdin.readline().upper().strip()
    elif choice == "D":
        frankston_models()
        sys.stdout.write(question)
        choice = sys.stdin.readline().upper().strip()
    elif choice == "E":
        a = a + 1
    else:
        sys.stdout.write("Please enter a valid response.\n")
        sys.stdout.write(question)
        choice = sys.stdin.readline().upper().strip()
                
sys.stdout.write("Goodbye")
