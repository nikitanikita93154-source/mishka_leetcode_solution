nums = [1,2,3,4,5,6,7,8,9,10]
big_ans=0
for n in nums:
    ans=0
    index=0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            index+=1
            ans+=i
            if n//i!=i:
                index+=1
                ans+=(n//i)
        if index>4:
            break
    if index==4:
        big_ans+=ans
print(big_ans)
