import sys
number_1 = 2
number_2 = 4
number_3 = 6

sys.stdout.write("Output 1: ")
answer = number_1 + number_2 + number_3 * 3
sys.stdout.write(str(answer))
# answer is 2+4=6
#           6*3=24

sys.stdout.write("\nOutput 2: ")
answer = (number_1 + number_2 + number_3) % 8
sys.stdout.write(str(answer))
# answer is 2+4+6=12
#           12%8 = 4
#8 goes into 12 once and leaves a remainder of 4


number_3 -= 1


sys.stdout.write("\nOutput 3: ")
answer = (number_1 * number_2 // number_3) + 1
sys.stdout.write(str(answer))

# 2*4 /5 = 1 + 1 = 2
#int division does not use decimal

                 
