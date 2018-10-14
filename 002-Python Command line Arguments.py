# 1-> Reads two numbers from input and typecasts them to int using
# list comprehension
x, y = [int(x) for x in input().split()]
print(x)
print(y)


# For this use cmd python file_name.py first second.
# 2->Python code to demonstrate the use of 'sys' module
# for command line arguments
import sys
# command line arguments are stored in the form
# of list in sys.argv
argumentList = sys.argv
print (argumentList)
# Print the name of file
print (sys.argv[0])
# Print the first argument after the name of file
print (sys.argv[1])

# factorial print use argv with cmd
import sys
from math import factorial
print(factorial(int(sys.argv[1])))
