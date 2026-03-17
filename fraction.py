#Creating data type 'fraction'

import math #for gcd(Greatest Common Divisor)
class Fraction:

  def __init__(self,n,d): #n as numerator, d as denominator

    #isinstance checks whether n is integer or not
    if not isinstance(n,int) or not isinstance(d,int):
      raise TypeError("Numerator and denominator must be integers")

    if d == 0:
      raise ValueError("Denominator cannot be zero")

    self.num = n
    self.den = d
  
  def __str__(self):
    return f"{self.num}/{self.den}"
    # return "{}/{}".format(self.num,self.den) Another way of using string formatting
  
  def __add__(self, other): #other is needed as we're doing for binary operator
    temp_num = self.num * other.den + other.num * self.den
    temp_den = self.den * other.den
    return self.simplify(temp_num,temp_den)

  def __sub__(self,other):
    temp_num = self.num * other.den - other.num * self.den
    temp_den = self.den * other.den
    # return f"{temp_num}/{temp_den}"
    return self.simplify(temp_num,temp_den)
  
  def __mul__(self, other):
    temp_num = self.num * other.num
    temp_den = self.den * other.den
    return self.simplify(temp_num,temp_den)  
  
  def __truediv__(self, other):
    temp_num = self.num * other.den
    temp_den = self.den * other.num
    return self.simplify(temp_num,temp_den)
  
  def simplify(self,n,d):
    gcd = math.gcd(n,d)
    return Fraction(n // gcd, d // gcd)
  
frac1 = Fraction(10,20)
frac2 = Fraction(30,40)
frac3 = Fraction("a",2)

print(frac1)
print(frac2)
print(frac1+frac2)
print(frac1-frac2)
print(frac1*frac2)
print(frac1/frac2)
print(frac3)