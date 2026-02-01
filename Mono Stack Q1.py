prices = [8, 4, 6, 2, 3]
stack=[]
result=prices[:]

for i in range(len(prices)):
    while stack and prices[i]<=prices[stack[-1]]:
        idx=stack.pop()
        result[idx]=prices[idx]
    stack.append(i)


