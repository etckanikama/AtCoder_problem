N = int(input())
S = str(input())

if N % 2 == 0:#偶数の時処理を行う。
    if S[:N//2] == S[N//2:N]:
        print('Yes')
    else:
        print('No')
else:
    print('No')