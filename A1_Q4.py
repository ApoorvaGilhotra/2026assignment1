lower_limit = int(input("enter the the lower limit"))
upper_limit=int(input("enter the the uppeer limit"))
for number in range(lower_limit,upper_limit+1):
    if(number>1):
        for i in range(2,number):
            if(number%i==0):
                print(end="")
                break
        else:
            print(number)
