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


