'''
Python is one of the most preferred languages out there. Its brevity and high readability makes it so popular among all programmers.

'''
'''
# 1. In-Place Swapping Of Two Numbers.
x, y = 10, 20
print(x, y)
x, y = y, x
print(x, y)

# 2. Reversing a string in Python
# 1-
a ="GeeksForGeeks"
print("Reverse is", a[::-1])
# 2-
test = [1,3,5]
test.reverse()
print(test)
# 3-
for ele in reversed(test): print(ele)

# 3. Create a single string from all the elements in list
a = ["Geeks", "For", "Geeks"]
print("-".join(a))

# 4. Chaining Of Comparison Operators.
n = 10
result = 1 < n < 20
print(result)
result = 1 > n <= 9
print(result)

# 4. Print The File Path Of Imported Modules.
import os;
import socket;

print(os)
print(socket
'''

# 5. Use Of Enums In Python.
class MyName:
    Geeks, For, Geeks = range(3)

print(MyName.Geeks)
print(MyName.For)
print(MyName.Geeks)

# 6. Return Multiple Values From Functions.
def x():
    return 1, 2, 3, 4
a, b, c, d = x()
print(a, b, c, d)

# 7. Find The Most Frequent Value In A List.
test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
print(max(set(test), key = test.count))

# 8. Check The Memory Usage Of An Object.
import sys
x = 45789
print(sys.getsizeof(x))

# 9. Print string N times.
n = 2;
a ="GeeksforGeeks";
print(a * n);

# 10. Checking if two words are anagrams
from collections import Counter
def is_anagram(str1, str2):
     return Counter(str1) == Counter(str2)
print(is_anagram('geek', 'eegk'))

print(is_anagram('geek', 'peek'))

# 11. Inspect An Object In Python.
test = [1,3,5,6]
print(dir(test))

# 12.  Simplify If Statement.
if 1 in [1,3,4,5,6]:
    print("yes")
else:
    print("not")
# use Multiple condision like - if 2 or 4 or 6 in

# 13. Detect Python Version at Runtime
import sys
print(sys.version)

# 14. Calculate The Factorial Of Any Number In One Line.
import functools
res = (lambda k: functools.reduce(int.__mul__,range(1,k+1),1))(5)
print(res)

# 15. We can’t define Infinities right? But wait! Not for Python
# Positive Infinity
p_infinity = float('Inf')

if 99999999999999 > p_infinity:
    print("The number is greater than Infinity!")
else:
    print("Infinity is greatest")

# Negetive Infinity
n_infinity = float('-Inf')
if -99999999999999 < n_infinity:
    print("The number is lesser than Negative Infinity!")
else:
    print("Negative Infinity is least")
