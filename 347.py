nums=[3,0,2]
k=2
nums_s={}
for num in nums:
    if num not in nums_s:
        nums_s[num]=1
    else:
        nums_s[num]+=1
ans = sorted(nums_s,key=nums_s.get)
print(ans[::-1][:k])
