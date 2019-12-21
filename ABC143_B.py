N =int(input())
h = list(map(int, input().split()))

result=0
for i in range(N):
   for j in range(i+1,N):
       result += h[i]*h[j]

print(result)

       