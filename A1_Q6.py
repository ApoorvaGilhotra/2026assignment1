n=int(input())
rev=0

while(n>0):
    if(n>=1 and n<10**9):
        a=n%10
        n = n // 10
        print(a)
