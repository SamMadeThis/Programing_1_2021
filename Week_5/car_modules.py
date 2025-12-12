import sys

werribee = ['Toyota HiLux', 'Ford Ranger', 'Toyota RAV4', 'Mazda CX-5', 'Hyundai i30', 'Toyota LandCruiser', 'Kia Cerato', 'Mazda 3']
sunbury = ['Toyota RAV4', 'Isuzu D-Max', 'Mitsubishi Triton', 'Hyundai i30', 'Kia Cerato', 'Mazda 3', 'Mitsubishi ASX', 'Mitsubishi Outlander']
frankston = ['Toyota RAV4', 'Toyota Corolla', 'Isuzu D-Max', 'Hyundai i30', 'MG ZS', 'Infiniti', 'Citroen', 'MINI', 'Volvo', 'Jaguar']

# justify code block (main_menu) 
# ---------------------------------------
# menu is a description of the content saved within the function.
# Its a list of the menu options which will be displayed to the user,
# alternatively I could have used menu_options,
# car_menu_options but chose to keep it simple with description. 
def main_menu():
    line_break="\n" + "-"*50 + "\n"
    menu = line_break + "\n+++Car Menu Options+++\n\n"
    menu += "[1] View Cars available at all dealers\n" 
    menu += "[2] View Cars exclusive to Werribee\n"
    menu += "[3] View Cars exclusive to Sunbury\n"
    menu += "[4] View Cars exclusive to Frankston\n"
    menu += "[5] Quit\n"
    sys.stdout.write(menu)
    sys.stdout.write("\nEnter option:")
    
# justify the code block (def all_cars())
# --------------------------------------
# Function created to carry out one of the operations listed in the
# specifications. I named it all_cars, as I thought it was an accurate
# desciption of the operation, which is to list all of the items in the
# tuples.
def all_cars():
    all_cars_in_stock = werribee + sunbury + frankston
    sys.stdout.write ("\nAll cars in stock at Werribee, Sunbury and Frankston:\n")
    # justify the condition
    # ---------------------------------------------------------------------
    # 2 variables named i & j to start from zero and increase by 1 when looping
    # through each index of all_cars_stock list until it has reached the length of the list(which is all items in the list)

    i=0
    j=0
    while i < len(all_cars_in_stock):
        j = i+1
        # justify the condition
        # ---------------------------------------------------------------------
        # 2 variables named i & j to start from zero and increase by 1 when looping
        # through each index of all_cars_stock list until it has reached the length of the list(which is all items in the list)
        # the additional while below will iterate through each item of the list while comparing if there are duplicates against itself. 
        # The duplicates will be deleted.
        while j < len (all_cars_in_stock):
            if all_cars_in_stock[i] == all_cars_in_stock[j]:
                all_cars_in_stock.pop(j)
            else:
                j+=1
        i += 1
    k = 0
    while k < len(all_cars_in_stock):
        sys.stdout.write(str(all_cars_in_stock[k]) + "\n")
        k +=1

# justify the code block(werribee_cars())
# --------------------------------------
# Function created to carry out one of the operations listed in the
# specifications. I could have used werribee_exclusive_cars, werribee_only,
# but I thought this was sufficient considering I was looking to simplify the
# name while also keeping it descriptive. 
def werribee_cars():
    sys.stdout.write("\nCars available at Werribee:\n\n")
    # justify the condition
    # --------------------------------------------------------------------------------------
    # m is used as a simple variable to iterate as required through the while loop.
    # while loop will list the items within the list called until all items have been listed.
    m = 0
    while m < len(werribee):
        sys.stdout.write(str(werribee[m]) + "\n")
        m += 1
# justify the code block (sunburry_cars())
# --------------------------------------
# Function created to carry out one of the operations listed in the
# specifications. To keep the 3 exclusive functions consistant I used the same
# naming convention as werribee_cars.
# Alternatively, I could have called it exclusive_cars_sunbury but I thought
# this name was sufficient in this instance. 
def sunburry_cars():
    sys.stdout.write("\nCars available at Sunbury:\n\n")
    # justify the condition
    # --------------------------------------------------------------------------------------
    # m is used as a simple variable to iterate as required through the while loop.
    # while loop will list the items within the list called until all items have been listed.
    n = 0
    while n < len(sunbury):
        sys.stdout.write(str(sunbury[n])+ "\n")
        n += 1
# justify the code block (frankston_cars())
# --------------------------------------
# Function created to carry out one of the operations listed in the
# specifications. To keep the 3 exclusive functions consistant I used the same
# naming convention as werribee_cars. Alternatively, I could have named it
# exclusive_cars_frankston or frankston_only, however I thought this was
# sufficient in this instance. 
def frankston_cars():
    sys.stdout.write("\nCars available at Frankston:\n\n")
    # justify the condition
    # -------------------------------------------------------------------------------------
    # m is used as a simple variable to iterate as required through the while loop.
    # while loop will list the items within the list called until all items have been listed.
    o = 0
    while o < len(frankston):
        sys.stdout.write(str(frankston[o])+ "\n")
        o += 1

