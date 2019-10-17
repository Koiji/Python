import math
n = input('Enter number: ')
n = int(n)
s = 0
while n > 0:
    s = s + n % 10
    n = n // 10
print(s)
