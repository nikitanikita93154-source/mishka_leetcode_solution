ans=[]
def recurs(deep,current):
    if deep==0:
        a = current
        a1 = 0
        flag = 0
        for k in a:
            if k == '(':
                a1 += 1
            if k == ')':
                if a1 == 0:
                    #print('A')
                    flag = 1
                else:
                    a1 -= 1
        if flag == 0 and a1 == 0:
            ans.append(current)
        return
    b='()'
    for i in b:
        recurs(deep-1,current+f'{i}')
recurs(16,'')
print(ans)