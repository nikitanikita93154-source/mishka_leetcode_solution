height=[0,2,1,0,1,3,1,2,0,1]
n=len(height)
left=[0]*n
right=[0]*n
m_l=height[0]
m_r=left[0]
for i in range(n-1):
    m_l=max(m_l,height[i])
    left[i]=m_l
for i in range(n-1,0,-1):
    m_r=max(m_r,height[i])
    right[i]=m_r
ans=0
for i in range(n-1):
    j=min(left[i],right[i])
    print(j,height[i])
    if j>height[i]:
        ans+=j-height[i]
print(ans)