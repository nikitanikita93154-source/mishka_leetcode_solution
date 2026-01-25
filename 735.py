asteroids=[5,10,-5]
ans=[]
i=0
while i<len(asteroids):

    if asteroids[i]>0 and ans!=[]:
        ans.append(asteroids[i])
        i+=1
    elif asteroids[i]<0 and ans!=[]:

        if ans[- 1] < 0:
            ans.append(asteroids[i])
            i += 1
        elif ans[- 1] > 0:

            if ans[- 1] + asteroids[i] < 0:
                ans.pop()
                continue
            elif ans[- 1] + asteroids[i] > 0:
                i += 1
            else:
                ans.pop()
                i += 1
    else:
        ans.append(asteroids[i])
        i+=1
print(ans)
