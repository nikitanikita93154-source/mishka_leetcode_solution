s=[2,1,5,0,4,6]
f=sec=float('inf')
for n in s:
    print(f,sec)
    if n<f:
        f=n
    elif n<=sec :
        sec=n
    else:
        print(1)
