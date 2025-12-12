import sys
from surgery_display import display_queue
from surprise import easter_egg

patient_data = {'Linda': 'Dr Lau', 'Bob':'Dr Lovett', 'Andrew':'Dr Lau' ,'Anne':'Dr Brayne', 'Taif':'Dr Karl'}
sys.stdout.write("Welcome, please be advised the average wait time is 30 minutes\n\n")
display_queue()
sys.stdout.write("\nThank you for your patience, see you soon")


sys.stdout.write("To see the surprise, please enter 'yes'\n\n")
user_input = sys.stdin.readline().strip().lower()

if user_input == "yes":
    easter_egg()

