num=8
bin_num=bin(num)[2:]
i=j=ans=0

for j in range(len(bin_num)):
    if bin_num[j]=='1':
        ans=max(ans,j-i)
        i=j
print(ans)
