def lis(arr):
    n = len(arr)
    lis = [1] * n
    for i in range(1, n):
        for prev in range(0, i):
            if arr[i] > arr[prev]:
                lis[i] = max(lis[i], lis[prev] + 1)
    return max(lis)

if __name__ == '__main__':
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    print(lis(arr))