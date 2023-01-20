n=(input())
k=int(input())
x=[]
for i in range(int(n)):
    x.append(i)

if(k==0):
    print(n)
elif(k>0):
    y = x.copy()
    for a in range(0,k):

        for j in range(1,len(n)):

            x[j] = y[j - 1]
        c=len(y)-1
        b = y[c]
        x[0] = b
        y=x.copy()
    for k in range(len(x)):
        c=x[k]
        print(c,end="")
        
elif(k<0):
    for a in range(abs(k)):
    
    
        x.append(x.pop(0))
    for k in range(len(x)):
        c=x[k]
        print(c,end="")
    
