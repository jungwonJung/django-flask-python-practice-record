def plus(a, b):
  a = int(a)
  b = int(b)
  return a + b

def minus(a, b):
  a = int(a)
  b = int(b)
  return a - b

def multiply(a, b):
  a = int(a)
  b = int(b)
  return a * b

def division(a, b):
  a = int(a)
  b = int(b)
  return a / b

def reminder(a, b):
  a = int(a)
  b = int(b)
  return a % b

def negation(a):
  a = int(a)
  return -a

def power(a, b):
  a = int(a)
  b = int(b)
  return a ** b

print(plus(2,"4"))
print(plus(b="4",a=2))

print(minus(2,"4"))
print(minus(b="4",a=2))

print(multiply(2,"4"))
print(multiply(b="4",a=2))

print (division("4",2))
print (division(b=2,a="4"))

print(reminder(2,"4"))
print(reminder(b="4",a=2))

print(negation(2))
print(negation(a=2))

print(power(2,"4"))
print(power(b="4",a=2))
