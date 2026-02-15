students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
c=0
while sandwiches:
    if students[0]==sandwiches[0]:
        sandwiches.pop(0)
        students.pop(0)
        c=0
    else:
        students.append(students.pop(0))
        c+=1
    if c>len(students):
        break
print(c)