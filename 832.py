arr=[0,1,2]
left=0
right=len(arr)-2
while left<=right:
    mid=(left+right)//2
    if arr[mid-1]<arr[mid] and arr[mid]>arr[mid+1]:
        print(arr[mid])
        break
    if arr[mid]<arr[mid+1]:
        left=mid+1
    else:
        right=mid-1
print(arr[-1])