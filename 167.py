numbers=[-1,0]
target=-1
sum={}
ans=[]
for i in range(len(numbers)):
    if numbers[i] in sum:
        ans=[sum[numbers[i]],i+1]
    else:
        sum[target-numbers[i]]=i+1
print(ans)
