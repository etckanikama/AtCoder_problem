def main():
    S = str(input())

    for i in range(len(S)):
        if (i+1) % 2 == 0:
            if S[i] == "R" :
                print('No')
                return
        else:
            if S[i] == "L":
                print("No")
                return
    print("Yes")

if __name__ == "__main__":
    main()
