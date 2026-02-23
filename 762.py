left=6
right=10
ans=0
for i in range(left, right+1):
    print(i)
    num = bin(i)[2:]
    if num.count('1') in [2, 3, 5, 7, 11, 13, 17, 19]:
        ans += 1
print(ans)