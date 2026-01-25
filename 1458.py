nums1=[-1,-1]
nums2=[1,1]
dp=[[float('-inf') for _ in range(len(nums1)+1)] for _ in range(len(nums2)+1)]
print(dp)
for i in range(len(nums2)):
    for j in range(len(nums1)):
        p=nums1[j]*nums2[i]
        dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1],dp[i][j]+p,p)
print(dp[-1][-1])