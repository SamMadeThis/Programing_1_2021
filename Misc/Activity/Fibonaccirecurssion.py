import sys
def get_fib_at_v2(i):
    if ((i==1) or (i==0)):
        return i
    return get_fib_at_v2(i-1) + get_fib_at_v2(i-2)
sys.stdout.write("Enter position in the Fib sequence: ")
i = int (sys.stdin.readline())
answer=get_fib_at_v2(i)
sys.stdout.write(str(answer)+" is at "+str(i))


