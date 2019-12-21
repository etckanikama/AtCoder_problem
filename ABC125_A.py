import math
a,b,t = map(int,input().split())

t += 0.5
print(math.floor(t//a)*b)