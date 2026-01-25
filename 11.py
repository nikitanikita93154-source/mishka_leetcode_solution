s=[4,3,2,1,4]
i=0
j=len(s)-1
m=min(s[j], s[i]) * (j - i)
if j<2:
    m = min(s[j], s[i]) * (j - i)
    print(m)
while i<j:
    if s[j]>s[i]:
        i+=1
        if m<(min(s[j],s[i])*(j-i)):
            m=min(s[j],s[i])*(j-i)
    else:
        j-=1
        if m<(min(s[j],s[i])*(j-i)):
            m=min(s[j],s[i])*(j-i)
print(m)

