n=int(input())
d=0
if(n>=1 and n<10**9):
    while(n!=0):
        n=n//10
        d=d+1
    print(d)
