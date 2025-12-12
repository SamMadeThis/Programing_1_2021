import sys
sys.stdout.write("How old are you? ")
age =int(sys.stdin.readline())
age_year = 2021 - age
sys.stdout.write("You were born in " + str(age_year))
