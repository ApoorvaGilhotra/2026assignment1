n=input()
m=list(map(int,n))
l=[]
length=len(m)
lol=length+1
c=0
for k in m:
    l.append(k)
for i in m:
    a=length-m.index(i)
    s=length-i
    l[s]=a
for j in range(1,lol):
    if(m.count(j)==1):
        c=c+1
if(c==length):
    for k in l:
        print(k,end="")
