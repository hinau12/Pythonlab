p = int(input("enter the principle amount"))
r = int(input("enter the rate of interest"))
n = int(input("enter no of times interest is compounded"))
t = int(input("no of years"))
a = p * (1 + r / (100*n)) (n * t)
CI= a - p
print(round(CI,2))
