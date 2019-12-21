N,K = (int(x) for x in input().split(' '))
h = list(map(int,input().split()))

result = 0
for x in h:
    if x >= K:
        result +=1
print(result)
    