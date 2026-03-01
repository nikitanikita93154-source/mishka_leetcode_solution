n = 12
ans=1
mod=10**9+7
for i in range(2,n+1):
    ans=((ans<<(len(bin(i))-2))+i)%mod
print(ans)
