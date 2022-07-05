"""making a program on the paradox of (3n -1) where if you put any number as 
input, it will always end up on 1"""

n = int(input("Input a number to apply 3n + 1 rule: "))

while n != 1:
  if not n % 2 == 0:
    n = (n*3) + 1
  elif n % 2 == 0:
    n /= 2
  print (int(n))
