class Point:
    def __init__(self, x, y, a, b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        if self.x is None and self.y is None:
            return
        if self.y**2 != self.x**3 + a * x + b:
            #Test to see if y^2 = x^3 + ax + b holds true
            raise ValueError(f'({x},{y}) is not on the curve')
        
    # Equality Operator
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y \
        and self.a == other.a and self.b == other.b

    # Not Equality Operator - Exercise 2
    def __ne__(self, other):
        return self.x != other or self.y != other.y \
        or self.a != other.a or self.b != other.b

    # Addition Operator Overload
    def __add__(self, other):
        if self.a != other.a or self.b != other.b:
            raise TypeError(f'Points {self}, {other} are not on the same curve'

        #Infinity Point Addition - Return the non None point
        if self.x is None:
            return other

        if other.x is None:
            return self

        # If x coordinates match but y does not - negate.
        if self.x == other.x and self.y != other.y:
            return self.__class__(None, None, self.a, self.b)

        # s= (y2-y1) / (x2-x1)
        # x3= s^2-x1-x2
        # y3= s*(x1-x3)-y1
        if self.x != other.x:
            s = (other.y - self.y) / (other.x - self.x)
            x = pow(s,2) - self.x - other.x
            y = s * (self.x - x) - self.y
            return self.__class__(x, y, self.a, self.b)

        # Case 4: if we are tangent to the vertical line,
        # we return the point at infinity
        # note instead of figuring out what 0 is for each type
        # we just use 0 * self.x
        if self == other and self.y == 0 * self.x:
            return self.__class__(None, None, self.a, self.b)

        # Case 3: self == other
        # Formula (x3,y3)=(x1,y1)+(x1,y1)
        # s=(3*x1**2+a)/(2*y1)
        # x3=s**2-2*x1
        # y3=s*(x1-x3)-y1
        if self == other:
            s = (3 * self.x**2 + self.a) / (2 * self.y)
            x = s**2 - 2 * self.x
            y = s * (self.x - x) - self.y
            return self.__class__(x, y, self.a, self.b)

        
        
    
### Finite Field Library ###
class FieldElement:
    # Initialize the Finite Field Element Class
    def __init__(self, num, prime):
        if num >= prime or num < 0:
            # Check if the number is within a valid range (non-negative and less than the defined prime).
            # If not, raise a ValueError with a suitable error message.
            error = 'Num {} not in field range 0 to {}'.format(
                num, prime - 1)
            raise ValueError(error)
        self.num = num
        # Set the number and prime attributes of this object to the given inputs.
        self.prime = prime
    
    def __repr__(self):
        # Define a representation of the field element in a readable format for debugging and logging.
        return 'FieldElement_{}({})'.format(self.prime, self.num)
    
    def __eq__(self, other):
        if other is None:
            # Check for equality with a None object, should always return False.
            return False
        # Check for equality between this field element and another.
        # True if both have the same number and the same prime, false otherwise.
        return self.num == other.num and self.prime == other.prime  
    
    def __ne__(self, other):
        if other is None:
            # Check for equality with a None object, should always return False.
            return False
        # Check for inequality between this field element and another.
        # True if they have either different numbers or different primes.
        return self.num != other.num or self.prime != other.prime  
    
    def __add__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot add two numbers in different Fields')
        num = (self.num + other.num) % self.prime
        return self.__class__(num, self.prime)

    def __sub__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot subtract two numbers in different Fields')
        num = (self.num - other.num) % self.prime
        return self.__class__(num, self.prime)

    def __mul__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot multiply two numbers in different Fields')
        num = (self.num * other.num) % self.prime
        return self.__class__(num, self.prime)

    def __pow__(self, exponent):
        n = exponent % (self.prime - 1)
        num = pow(self.num, n, self.prime)
        return self.__class__(num, self.prime)

    def __truediv__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot divide two numbers in different Fields')
        # self.num and other.num are the actual values
        # self.prime is what we need to mod against
        # use fermat's little theorem:
        # self.num**(p-1) % p == 1
        # this means:
        # 1/n == pow(n, p-2, p)
        num = (self.num * pow(other.num, self.prime -2, self.prime)) % self.prime
        return self.__class__(num, self.prime)