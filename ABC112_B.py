N,T = map(int,input().split())

for i in range(N):
    re,te = list(map(int,input().split()))

for i in range(N):
    if te[i] > T:
        del re[i]
    
re.sort()
if re is None:
    print('TLE')
else:
    print(min(re))
        
