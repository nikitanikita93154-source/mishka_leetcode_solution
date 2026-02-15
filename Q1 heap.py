stones=[1]
while len(stones)>1:
    stones.sort(reverse=True)
    print(stones)
    if stones[0]==stones[1]:
        stones.pop(0)
        stones.pop(0)
    else:
        x=stones.pop(0)
        y=stones.pop(0)
        stones.append(x-y)
print(stones)
