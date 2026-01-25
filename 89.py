n = 16
gray_codes = [i ^ (i >> 1) for i in range(2**n)]
print(gray_codes[:10])
