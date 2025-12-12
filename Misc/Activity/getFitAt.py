import sys
def getFibAt(i): #return Fibonacci series value at i
   a, b=0, 1
   while i>0:
      a, b = b, a+b
      i-=1
   return a
sys.stdout.write("Enter a position in the Fibonacci sequence: ")
i = int( sys.stdin.readline() )
answer = getFibAt(i)
sys.stdout.write( str(answer)+" is at "+str(i))

def getFibAt():
   """This is a helpful paragraph which tells you.

   What this program does."""
   pass

#run the code and type help(getFibAt) so it brings up the docstring

def getFibAt(i:int)->int:
   print( getFibAt.__annotations__ )
 
print( getFibAt.__annotations__ )
