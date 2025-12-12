import sys

weekDays = ["Monday", "Tueday", "Wednesday", "Thursday", "Friday"]

day = 0

while (day < len(weekDays)) : # (0<5) True
    sys.stdout.write("\n" + weekDays[day])
    day += 1
