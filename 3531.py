arr = [[1,3],[3,2],[3,3],[3,5],[5,3]]
sorted_arr_y = sorted(arr, key=lambda x: x[1])
sorted_arr_x = sorted(arr, key=lambda x: x[0])
q=[]
ans=0
if len(sorted_arr_y)-2>0:
    for i in range(1,len(sorted_arr_y)):
        if sorted_arr_y[0][1]<sorted_arr_y[i][1]<sorted_arr_y[-1][1]:
            q.append((sorted_arr_y[i][0],sorted_arr_y[i][1]))
if len(sorted_arr_x)-2>0:
    for i in range(1,len(sorted_arr_x)):
        if sorted_arr_x[0][0]<sorted_arr_x[i][0]<sorted_arr_x[-1][0] and (sorted_arr_x[i][0],sorted_arr_x[i][1]) in q:
            ans+=1

print(ans)
