import sys
    
def identify_common_items(list1,list2):
    
    i=0
    while (i<len(list1)):
        j=0
        while(j<len(list2)):
            if (i==j):
                sys.stdout.write(str(i)+"vs"+str(j)+" ")
            j+=1
        i+=1
    


def identify_food(list1,list2,list3):

    i=0
    while (i<len(list1)):
        matches = 0
        j=0
        while(j<len(list2)):
            if j=="food":
                matches+=1
                sys.stdout.write("Found 1 match from list 2")
            j+=1
        j=0
        while(j<len(list3)):
            if j=="food":
                matches+=1
                sys.stdout.write("Found 1 match from list 3")
            if (no matches):
                display item from list 1 at i as unique
        i+=1




