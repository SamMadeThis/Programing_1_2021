import sys

werribee = {"Venue", "Kona", "Tucson", "Santa Fe"} 

sunbury = {"i30", "Kona", "Santa Fe", "Palisade"}

frankston = {"Venue", "Kona", "Tucson", "Santa Fe", "Palisade", "Ioniq",
              "i30", "Staria"}

message = "These are the cars available at {}:"

dashes = "=" * 10

def all_car_models():
    all_in_stock = werribee | sunbury | frankston
    sys.stdout.write(message.format("Werribee, Sunbury and Frankston"))
    sys.stdout.write("\n" + dashes.center(80))
    for i in all_in_stock:
        sys.stdout.write("\n" + i.center(80))
    sys.stdout.write("\n" + dashes.center(80))        

def werribee_models():
    sys.stdout.write(message.format("Werribee"))
    sys.stdout.write("\n" + dashes.center(80))
    for j in werribee:
        sys.stdout.write("\n" + j.center(80))
    sys.stdout.write("\n" + dashes.center(80) + "\n")

def sunbury_models():
    sys.stdout.write(message.format("Sunbury"))
    sys.stdout.write("\n" + dashes.center(80))
    for k in sunbury:
        sys.stdout.write("\n" + k.center(80))
    sys.stdout.write("\n" + dashes.center(80) + "\n")

def frankston_models():
    sys.stdout.write(message.format("Frankston"))
    sys.stdout.write("\n" + dashes.center(80))
    for l in frankston:
        sys.stdout.write("\n" + l.center(80))
    sys.stdout.write("\n" + dashes.center(80) + "\n")
