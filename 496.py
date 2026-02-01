from string import ascii_uppercase

nums1=[4,1,2]
nums2=[1,3,4,2]
stack=[]
n={}
ans=[]
for i in range(len(nums2)):
    while stack and nums2[i]>nums2[stack[-1]]:
        num=nums2[stack.pop()]
        n[num]=nums2[i]
    stack.append(i)
print(n)
for i in nums1:
    if i in n:
        ans.append(n[i])
    else:
        ans.append(-1)
print(ans)