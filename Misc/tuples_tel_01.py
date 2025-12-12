#3.3.2 Introducing stacks and queues
from collections import deque

patientsQueue = []

patientsQueue = deque(["Eric", "John", "Michael"])
print (patientsQueue)

print("Terry has arrived.")
patientsQueue.append("Terry")       
print (patientsQueue)

print ("The doctor has called the first patient in")
patientsQueue.popleft()
print (patientsQueue)


print("Garry has arrived.")
patientsQueue.append("Garry")       
print (patientsQueue)

print ("The doctor has called the called new arrival")
patientsQueue.pop()
print (patientsQueue)

print ("The doctor has called the patient patient in")
patientsQueue.popleft()                 
print (patientsQueue)

print ("The doctor has called the patient patient in")
patientsQueue.popleft()                 
print (patientsQueue)

patientsQueue                           # Remaining queue in order of arrival
# ---------------------------------------------------------------------------------------------------
# 4.1.2 Creating dictionaries
# If we use a list, we can create two lists: one for storing the client’s names,
# and another for their phone numbers.
names = ['jack','sape']
tel_nums = [409638642,413983635]
# Let’s assume that we need to print the phone number of ‘jack’.
# To do this, we must first find the index of ‘jack’ in the names list as follows:
index_of_client = names.index('jack')
# We can then use the value stored in index_of_client to retrieve that client’s number from the nums list:
print ( tel_nums[index_of_client] )
# Alternatively, we can simplify this further without using the index_of_client variable as follows:
print ( tel_nums[names.index('jack')] )
#bThis code looks up the index of the ‘jack’ value in the names list,
# then returns the value at the same index in the tel_nums list.

#----------------------------------------------------------------------------------------------------

# Instead of the above list-based approach, we could create a dictionary named tel which has both the name
# and the number of a client. A dictionary is a set of pairs (each consisting of a key and a value),
# that allows us to return the value simply by providing the key:
print ( tel_nums['jack'] )
