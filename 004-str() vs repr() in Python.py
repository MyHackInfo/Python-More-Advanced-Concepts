# str() and repr() both are used to get a string representation of object.
s = "this is string"
print(str(s))
print(str(2.0/11.0))

print(repr(s))
print(repr(2.0/11.0))


# Python program to demonstrate writing of __repr__ and
# __str__ for user defined classes

# A user defined class to represent Complex numbers
class Complex:

    # Constructor
    def __init__(self, real, imag):
       self.real = real
       self.imag = imag

    # For call to repr(). Prints object's information
    def __repr__(self):
       return 'Rational(%s, %s)' % (self.real, self.imag)

    # For call to str(). Prints readable form
    def __str__(self):
       return '%s + i%s' % (self.real, self.imag)


# Driver program to test above
t = Complex(10, 20)

print (str(t))  # Same as "print t"
print (repr(t))
