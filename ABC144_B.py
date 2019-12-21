def main():
    N = int(input())
    #N = int(a)*int(b)
    a = [1,2,3,4,5,6,7,8,9]
    b = [1,2,3,4,5,6,7,8,9]
    for s in a:
        #print(s)
        for w in b:
        # print("s={},w={}".format(s,w))
            
            if N == s * w:
                print('Yes')
                return
    print('No')
               
        
if __name__ == "__main__":
    main()
        