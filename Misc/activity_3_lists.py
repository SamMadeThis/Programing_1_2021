import sys

# what is the output?

weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

sys.stdout.write("Output 1: ")
sys.stdin.readline()
sys.stdout.write(weekDays[2])


sys.stdout.write("\n\nOutput 2: ")
sys.stdin.readline()
sys.stdout.write(weekDays[-2])

sys.stdout.write("\n\nOutput 3: ")
sys.stdin.readline()
sys.stdout.write(str(len(weekDays)))
