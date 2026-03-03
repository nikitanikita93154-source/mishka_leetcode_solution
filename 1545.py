def findKthBit(n,k):
    if n==1:
        return '0'
    lenght = (1 << n) - 1
    mid = (lenght + 1) // 2
    if k == mid:
        return '1'
    if k < mid:
        return findKthBit(n - 1, k)
    c = findKthBit(n - 1, lenght - k + 1)
    return '1' if c == '0' else '0'
print(findKthBit(3,3))