arr=[9,4,2,10,7,8,8,1,9]
c=best=0
for i in range(len(arr)):
    if i>=2 and (arr[i-2]<arr[i-1]>arr[i] or arr[i-2]>arr[i-1]<arr[i]):
        c+=1
    elif i>=1 and (arr[i-1]>arr[i] or arr[i-1]<arr[i]):
        c=2
    else:
        c=1
    best=max(best,c)
print(best)



