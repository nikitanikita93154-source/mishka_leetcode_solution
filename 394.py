s='3[a]2[bc]'
stack=[]
str=''
number=0
ans=''
for i in s:
    if i.isdigit():
        number=number*10+int(i)
    elif i=='[':
        stack.append(str)
        stack.append(number)
        str=''
        number=0
    elif i==']':
        num=stack.pop()
        ans=stack.pop()
        str=ans+(num*str)

    else:
        str+=i
print(str)