s=[0,0,0,0,1]
i=0
index=0
if s==[1] :
    print('s')
while i+1<len(s):
    print('a',i)
    if i==0:
        if s[i]==0 and s[i+1]==0:
            s[i]=1
            i+=2
            index+=1
    elif s[i-1]==0 and s[i+1]==0 and s[i]==0:
        s[i]=1
        i+=2
        index+=1
    else:
        i+=1
    print('b', i, index, s)
if s[0] == 0 and s[1] == 0:
    index += 1
    s[0]=1
if s[-1]==0 and s[-2]==0:
    s[-1]=1
    index+=1
print(index)