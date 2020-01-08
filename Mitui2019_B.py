import math
n = int(input())

x = n /1.08
price= math.ceil(x)

if math.floor(price*1.08) == n:
    print(price)
else:
    print(':(')
