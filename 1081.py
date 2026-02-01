s="cbacdcbc"
last_occurrence = {char: i for i, char in enumerate(s)}
stack=[]
in_stack=set()
for i,char in enumerate(s):
    if s[i] in in_stack:
        continue
    else:
        while stack and ord(stack[-1])>ord(s[i]) and last_occurrence[stack[-1]] > i:
            removed=stack.pop()
            in_stack.remove(removed)
    stack.append(char)
    in_stack.add(char)
print(stack)
