word1='abcsss'
word2='pqr'
i=j=0
l1=len(word1)
l2=len(word2)
merged=''
while i<len(word2) and i<len(word1):
    merged+=word1[i]
    merged += word2[i]
    i+=1
merged+=word2[i:]+word1[i:]

print(merged)