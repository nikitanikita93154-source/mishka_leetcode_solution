n=3
ans=[1,2,5]
for i in range(3,n):
    a=ans[i-1]*2+ans[i-3]
    ans.append(a)
print(ans[n-1])