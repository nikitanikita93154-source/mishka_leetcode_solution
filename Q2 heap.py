import heapq as heap
nums1=[1,1,2]
nums2=[1,2,3]
k=2
resV=[]
pq = []
for x in nums1:
    heap.heappush(pq, [x + nums2[0], 0])
while k > 0 and pq:
    pair = heap.heappop(pq)
    s, pos = pair[0], pair[1]
    resV.append([s - nums2[pos], nums2[pos]])
    if pos + 1 < len(nums2):
        heap.heappush(pq, [s - nums2[pos] + nums2[pos + 1], pos + 1])
    k -= 1
print(resV)
