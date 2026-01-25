nums=[0]
index = 0
ans = 0
for i in range(len(nums)):
    if nums[i] == 1:
        index += 1
        continue
    else:
        if index > ans:
            ans = index
        index = 0
if ans>index:
    print(ans)
else:
    print(index)
