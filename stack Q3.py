n=2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
ans=[0]*n
stack=[]
for log in logs:
    fn,com,tm=log.split(':')
    fn,tm=int(fn),int(tm)
    if com=='start':
        if stack:
            ans[stack[-1]]+=tm-prev_time
        stack.append(fn)
        prev_time=tm
    else:
        ans[stack.pop()]+=tm-prev_time+1
        prev_time=tm+1
print(ans)
