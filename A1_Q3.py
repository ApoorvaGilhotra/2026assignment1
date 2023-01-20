t=int(input())
for i in range(0,t):
   
    n=int(input())
    
    if(n>1):
        for j in range(2,n):
            if(n%j==0):
                print("not prime")
                break
        else:
            print("prime")
    elif(n==1):
        print("not prime")
                 
