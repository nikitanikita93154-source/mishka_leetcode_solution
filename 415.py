nums1='11'
nums2='999999'
a=''
b=''
if len(nums2)>len(nums1):
    a=nums2[::-1]
    b=nums1[::-1]
else:
    a = nums1[::-1]
    b = nums2[::-1]
i = 0
j = 0
carry = 0
res = ''

while j < len(a) or i < len(b) or carry:
    digit_a = int(a[j]) if j < len(a) else 0
    digit_b = int(b[i]) if i < len(b) else 0

    total = digit_a + digit_b + carry
    digit = total % 10
    carry = total // 10

    res += str(digit)

    i += 1
    j += 1
result = res[::-1]
print(result)
