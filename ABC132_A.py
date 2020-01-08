s=str(input())
if s[0] != s[1]:
    if s.count(s[0]) == 2 and s.count(s[1])==2:
        print("Yes")
    else:
        print("No")
elif s.count(s[0])==2 and s.count(s[3]) == 2:
    print("Yes")
else:
    print("No")