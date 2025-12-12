import sys

students = {"student1": 1, "student2": 2, "student3": 3}

# looping through dictionary
sys.stdout.write ("\n---------------------------------------------")

# using string concatenation
for key, value in students.items():
    sys.stdout.write(key + ", " + str(value) + ". ")

# using a formatting string literal
for key, value in students.items():
    sys.stdout.write(f"\n{key:10} --> {value:3d}")

# ---------------------------------
fruit = "Apple"
# using string concatenation
details = "\n"
details += fruit
details += " has "
details += str(len(fruit))
details += " letters, it starts with "
details += fruit[0] + "."

sys.stdout.write(details)

# usihng string format() method
# With str.format(), the replacement fields are marked by curly braces
details = "\n{} has {} letters, it starts with {}."
details = details.format(fruit, len(fruit), fruit[0])
sys.stdout.write(details)

# alternative way to format strings
sys.stdout.write("\n" + fruit.rjust(10))
sys.stdout.write("\n" + fruit.ljust(10))
sys.stdout.write("\n" + fruit.center(10))

sys.stdout.write("\n" + fruit.rjust(10, "*"))
sys.stdout.write("\n" + fruit.ljust(10, "@"))
sys.stdout.write("\n" + fruit.center(10, "="))
