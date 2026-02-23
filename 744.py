letters = ["x","x","y","y"]
target = "z"
left=0
right=len(letters)-1
res=None
while left<=right:
    mid=(left+right)//2
    if letters[mid]>target:
        res=letters[mid]
        right=mid-1
    else:
        left=mid+1
if res:
    print(res)
print(letters[0])