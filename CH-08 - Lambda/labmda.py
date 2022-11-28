# Python Lambda

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.


x = lambda a : a + 10
print(x(5))

x1 = lambda a,b,c : a+b+c
print(x1(1,2,3))

# With Function

def labmda_funct(n):
  return lambda a : a * n

square = labmda_funct(10)
print(square(10))