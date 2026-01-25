nums=[0,1,1]
p=''
ans=[]
for i in nums:
        p+=f'{i}'
        ans.append(int(p,2)%5==0)
print(ans)