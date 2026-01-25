happiness = [2,3,4,5]
k = 1
ans=0
for i in range(0,k):
    h=happiness[-i-1]
    if h-i>=0:
        ans+=(h-i)
    else:
        break
print(ans)