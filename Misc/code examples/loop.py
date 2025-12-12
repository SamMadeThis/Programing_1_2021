import sys

def main_page():





    name = 0
    
    while True:
        if name == 0:
            sys.stdout.write("Enter your name: ")
            name = sys.stdin.readline().strip()


        if (name == ""):
            sys.stdout.write("\nNo name was entered")
            name = sys.stdin.readline().strip()


        else:
            sys.stdout.write("\nWelcome " + name + "!\n")
            name = sys.stdin.readline().strip()

main_page()
       
