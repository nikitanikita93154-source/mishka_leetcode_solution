import math
s=122122
r=int(math.sqrt(s))
while s%r!=0:
    r-=1
print(s//r,r)
low = 0
high = len(r) - 1
print(low)