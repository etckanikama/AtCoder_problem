N = input().split(' ')
A = int(N[0])
B = int(N[1])
C = int(N[2])
x = A -B
result = C - x
if result < 0:
    print(int('0'))
else:
    print(result)


