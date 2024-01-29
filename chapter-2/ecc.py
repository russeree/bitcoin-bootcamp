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