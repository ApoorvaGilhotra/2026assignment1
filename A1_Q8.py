n=(input())
k=int(input())
x=list(map(int,n))

if(k==0):
    print(n)
elif(k>0):

    for j in range(1,len(n)):

        x[j]=x[j-1]

    for i in range(k):
        a = int(n) % 10

        x[i] = a

    for k in range(x):
        print(k,end="")
