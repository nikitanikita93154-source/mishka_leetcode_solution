s=[2,0]
i=0
j=1
while j<len(s):
    if s[i]>s[j]:
        print('a',s[i],s[j])
        while j-1>=0 and s[j-1]>s[j]:
            s[j-1],s[j]=s[j],s[j-1]
            print('b',s[i],s[j])
            j-=1
        j=i+1
    elif s[i]<=s[j]:
        i+=1
        j+=1
    print(s)
print(s)

