import sys
isCommuting = False
isHeavyTraffic = False
if isCommuting and isHeavyTraffic:
  sys.stdout.write("You are going to be late for work. ")
if isCommuting or isHeavyTraffic:
  sys.stdout.write("You are in a car. ")
if not isCommuting:
  sys.stdout.write("You are not commuting. ")

