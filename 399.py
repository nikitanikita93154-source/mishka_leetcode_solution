equations=[["a","b"],["b","c"]]
values=[2.0,3.0]
quries=[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
g={}
for (a, b), v in zip(equations, values):
    g.setdefault(a, {})[b] = v
    g.setdefault(b, {})[a] = 1.0 / v
def dfs(x,y):
    if x not in g or y not in g:
        return -1
    s=[[x,1.0]]
    visited=set()
    while s:
        c,r=s.pop()
        if c==y:
            return r
        visited.add(c)
        for i in g[c]:
            if i not in visited:
                s.append([i,r*g[c][i]])
    return -1
print([dfs(a,b) for a,b in quries])
