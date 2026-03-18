#Creating data type 'fraction'

import math #for gcd(Greatest Common Divisor)
class Fraction:

  def __init__(self,n,d): #n as numerator, d as denominator

    #isinstance checks whether n is the type written on it or not
    if not isinstance(n,int) or not isinstance(d,int):
      raise TypeError("Numerator and denominator must be integers")

    if d == 0:
      raise ValueError("Denominator cannot be zero")

    #stores unsimplified numerator and denominator 
    self.num = n 
    self.den = d 

    # Keep denominator positive
    if self.den < 0:
      self.num *= -1
      self.den *= -1
  
  def __str__(self):
    return f"{self.num}/{self.den}"
    # return "{}/{}".format(self.num,self.den) Another way of using string formatting
  
  #runs when __str__ method is not found
  #__repr__ is mainly used for debugging as output is diff from __str__
  def __repr__(self):
      return f"Fraction({self.num}, {self.den})"
  
  #Simplify
  def simplify(self):
    gcd = math.gcd(self.num,self.den)
    return Fraction(self.num // gcd, self.den // gcd)

  #Convert int into fraction (if needed)
  # Internal helper method (underscore means for internal use)
  # Ensures 'other' is a Fraction (converts int to Fraction if needed)
  def _convert(self, other):
    if isinstance(other,int):
      return Fraction(other,1)
    if isinstance(other,Fraction):
      return other
    raise TypeError("Unsupported type")
  
  #Arithmetic operations
  def __add__(self, other): #other is needed as we're doing for binary operator
    other = self._convert(other)
    temp_num = self.num * other.den + other.num * self.den
    temp_den = self.den * other.den
    return Fraction(temp_num,temp_den).simplify()

  def __sub__(self,other):
    other = self._convert(other)
    temp_num = self.num * other.den - other.num * self.den
    temp_den = self.den * other.den
    # return f"{temp_num}/{temp_den}"
    return  Fraction(temp_num,temp_den).simplify()
  
  def __mul__(self, other):
    other = self._convert(other)
    temp_num = self.num * other.num
    temp_den = self.den * other.den
    return  Fraction(temp_num,temp_den).simplify() 
  
  def __truediv__(self, other):
    other = self._convert(other)
    temp_num = self.num * other.den
    temp_den = self.den * other.num
    return  Fraction(temp_num,temp_den).simplify()

  
#Testing
frac1 = Fraction(10,-2)
frac2 = Fraction(30,3)

print(frac1)
print(frac2)

print("Addition")
print(frac1+frac2)
print("Substraction")
print(frac1-frac2)
print("Multiplication")
print(frac1*frac2)
print("Division")
print(frac1/frac2)

print("Example for _convert method")
print(frac1 * 2)