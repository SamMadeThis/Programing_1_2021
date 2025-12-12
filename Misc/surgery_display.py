import sys

patient_data = {'Linda': 'Dr Lau', 'Bob':'Dr Lovett', 'Andrew':'Dr Lau' ,'Anne':'Dr Brayne', 'Taif':'Dr Karl'}
    

def display_queue():
        sys.stdout.write("Patient information: \n")
        for x, y in patient_data.items():
                print(x, 'will see', y)


