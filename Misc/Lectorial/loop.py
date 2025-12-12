import sys

my_list = ["Hello", "World", "out", "there"]
index=0
if (index < len(my_list)):

    sys.stdout.write(str(index) + " contains " +my_list[index] + "\n\n")
    index+=1
