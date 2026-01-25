s=["a"]
i=0
j=index=index2=1
while i<len(s) and j<len(s):
    if s[i]==s[j]:
        j+=1
        index+=1
    elif s[i]!=s[j]:
        s[index2-1]=s[i]
        if index==1:
            pass
        else:
            for i in str(index):
                s[index2]=i
                index2+=1
        index2+=1
        i=j
        j+=1
        index=1
s[index2-1]=s[i]
if index == 1:
    print(index2)
else:
    for i in str(index):
        s[index2] = i
        index2 += 1
    print(index2)
