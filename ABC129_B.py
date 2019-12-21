n = int(input())
w = list(map(int,input().split()))

L=[]
for i in range(n):
    a = sum(w[:i])
    b = sum(w) - sum(w[:i])
    L.append(abs(a-b))
print(min(L))     



