a=1
b=2
c=1000
binary_a= f"{a:0{len(bin(max(a,b,c)))}b}"
binary_b=f"{b:0{len(bin(max(a,b,c)))}b}"
binary_c=f"{c:0{len(bin(max(a,b,c)))}b}"
ans=0
for i in range(len(bin(max(a,b,c)))-1,-1,-1):
    if int(binary_b[i]) | int(binary_a[i])!=int(binary_c[i]):
        if int(binary_c[i])==1:
            ans+=1
        elif int(binary_c[i])==0 and (int(binary_b[i])==0 or int(binary_a[i])==0):
            ans+=1
        else:
            ans+=2
print(ans)