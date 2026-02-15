tickets = [2,3,2]
k = 2
ans=0
while k>=0 and tickets[k]>0 :
    if k==0 and tickets[k]==1:
        ans+=1
        break
    t=tickets.pop(0)-1
    ans += 1
    if t>0:
        tickets.append(t)
    if k==0:
        k=len(tickets)-1
    else:
        k-=1
print(ans)
