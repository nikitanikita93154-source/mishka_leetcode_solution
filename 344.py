s=["h","e","l","l","o"]
right = len(s) - 1
left = 0
while left < right-1:
    a = s[left]
    b = s[right]
    s[left] = b
    s[right] = a
    right-=1
    left+=1
print(s)
