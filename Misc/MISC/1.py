import sys

def main():
    """track how much water water is ingested over
    7 days using tuple functions

    """
water_mls = ()
consumption = []
# water in millilitres

x=0
# x will represent day of week starting on monday
while x < 8:
#
# the paramaters are 7 days always, so a While loop is sufficient for
# until completed function
    day=("monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",)
    sys.stdout.write("\n"+day[x]+"\n")
    # as x+, index value of day increases+1
    #
    consumption=int(sys.stdin.readline())
    # as this requires number input, an int is required.
    x+= 1
    if x is 7:
    # 
        sys.stdout.write("\nThis is your Water consumption for 7 days\n"
                             +(str(consumption)))
    #
    # traceback error in line 18. the index value implementation needs work
    #
main()
