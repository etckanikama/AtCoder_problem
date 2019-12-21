n = int(input())
a = list(map(int,input().split()))

ans= 0
for x in range(n):
    ans += 1/a[x]
print(1/ans)