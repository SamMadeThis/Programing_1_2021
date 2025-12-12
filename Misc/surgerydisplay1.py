import sys

patients = ["Linda", "Bob", "Andrew", "Anne", "Taif"]
doctors = ["Dr Lau", "Dr Lovett", "Dr Brayne"]


sys.stdout.write("Patients currently in the waiting room: \n")
for x, y in zip(patients, doctors):
    print('{0} will see {1}.' .format(x, y))
