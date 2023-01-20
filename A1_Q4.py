low=int(input())
high=int(input())
for number in range(low,high+1):
    if(number>1):
        for i in range(2,number):
            if(number%i==0):
                print(end="")
                break
        else:
            print(number)
