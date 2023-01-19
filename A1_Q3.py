low = int(input())
high = int(input())

for n in range(low, high + 1):
    if (low >= 2 and low < high and high < 10 ** 6):
        if (n > 1):
            for i in range(2, n):
                if (n % i == 0):
                    print(end="")
                    break
            else:
                print(n)
