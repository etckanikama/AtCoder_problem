def main():
    s= str(input())
    n = int(len(s))
    num = 0
    for i in range(n//2):
        if s[i] != s[-i-1]:
            num += 1
    print(num)               

if __name__ == "__main__":
    main()
