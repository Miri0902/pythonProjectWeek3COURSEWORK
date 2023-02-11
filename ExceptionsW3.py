# 1. perimeter of a rectangle
def perimeter_rectangle(w : int, h : int):
    if w < 0:
        raise ValueError("the given width %d is negative" %w)
    if h < 0:
        raise ValueError("the given height %d is negative" %h)
    return 2*(w+h)
try:
    print("Let's calculate the perimeter of a rectangle!")
    w = int(input("Enter the width:"))
    h = int(input("Enter the height:"))
    p= perimeter_rectangle(w, h)
    print("The perimeter is: %d" %p)
except ValueError as err:
    print("invalid input: %s" %err)

# square root
#write in python function calc_sqrt (k) which calculates the square root of a given
#number k, raising a vale error if k is negative. This requires function sqrt from
#the math module

from math import sqrt
def square_root  (n : int):
    if n < 0:
        raise ValueError("the given number %d is negative" %n)
    return sqrt(n)
try:
    print("Please input positive number")
    n = int(input("enter a number:"))
    r = square_root(n)
    print("The square root is: %d" %r)
except ValueError as err:
    print("invalid input: %s" %err)

#3. least common multiple
# in prevous excercises we did least common multiple, Try the following:
# print(lcm(6,0)). What output do we get?
# then Add a try/except block to handle the exception. Include a message to the
#user that the value given is invalid

def lcm(x, y):
  if x > y:
      z = x
  else:
      z = y
  while(True):
      if((z % x == 0) and (z % y == 0)):
          lcm = z
          break
      z += 1
  return lcm
print(lcm(4, 6))
print(lcm(15, 17))



# lcm
def div_many (p, qs):
    r =[]
    try:
        for q in qs:
            r.append(p/q)
    except ZeroDivisionError:
        r = []
    return r
print("the least common multiple")



