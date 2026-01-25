nums=[8,4,2,8,4]
ans=0
memo, duplets = {}, {}
res = 0
MOD = 10 ** 9 + 7

for number in nums:
    print(memo,duplets)
    res = (res + duplets.get(number, 0)) % MOD
    twon = number * 2
    if twon in memo:
        duplets[twon] = (duplets.get(twon, 0) + memo[twon]) % MOD
    memo[number] = memo.get(number, 0) + 1

print(duplets,memo)
print(res)