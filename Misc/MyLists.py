import sys
countries = ["Japan", "Argentina", "Belgium", "Norway", "Sweden"]
fun = ["Reading", "Bubble baths", "Gardening", "Netflix", "Bowling"]

# countries list length
sys.stdout.write("Output 1: Countries List ")
sys.stdout.write(str(len(countries)))

# while loop on countries list
c = 0

while (c < len(countries)):
    sys.stdout.write("\n\n" + countries[c])
    c += 1

# c+=1 to cut the infinite loop, the program will print just once 


    
# fun list length

sys.stdout.write("\n\nOutput 2: Fun List ")
sys.stdout.write(str(len(fun)))
# while loop on fun list
f = 0

while (f < len(fun)):
    sys.stdout.write("\n\n" + fun[f])
    f += 1
