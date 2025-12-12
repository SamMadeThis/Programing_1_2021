import sys

sys.stdout.write ("Enter ID: ")
roleID=int(sys.stdin.readline())
sys.stdout.write("Enter ID "+str(roleID) +"'s role: ")
role=sys.stdin.readline().strip()
sys.stdout.write("Hello "+role+" 00"+str(roleID))

#its important to note that .strip() is an inbuilt function we can use on input to strip the new line characters #
#when you print the input it will be displayed on the same line as your string instead of on a new line
# INT automatically strips the input
# .strip on a strip will be best practice

sys.stdout.write ("Enter ID: ")
roleID=int(sys.stdin.readline())
sys.stdout.write("Enter ID "+str(roleID) +"'s role: ")
role=sys.stdin.readline()
sys.stdout.write("Hello "+role+" 00"+str(roleID))
