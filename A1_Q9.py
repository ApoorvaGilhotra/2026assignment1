num1=int(input())
num2=int(input())
if(num1>num2):
    smaller=num2
else:
    smaller=num1
for i in range(1,smaller+1):
    if(num1%i==0 and num2%i==0):
        hcf=i
    else:
        smaller=smaller+1
print(hcf)

if(num1>num2):
    greater=num1
else:
    greater=num2
while (True):
    if(greater%num1==0 and greater%num2==0):
        print(greater)
        break

    else:
        greater=greater+1

