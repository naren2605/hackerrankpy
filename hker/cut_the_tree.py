# Enter your code here. Read input from STDIN. Print output to STDOUT
visited=dict()
def getneighbours(edgelist,v):
    if edgelist.has_key(v):
        for key in edgelist[v]:
            yield key
def root(span):
    r=None
    for key in span:
        r=key
        break
    while span.has_key(r):
        r=span[r]
    return r
def dfs(graph,start):
    count=0
    stack=list()
    stack.append(start)
    spanning=dict()
    leafs=list()
    while len(stack)!=0:
        v=stack.pop()
        if not visited.has_key(v):
            count=count+lst[v-1]
            visited[v]=True
            children=0
            for vx in getneighbours(graph,v):
                if not visited.has_key(vx):
                    children=children+1
                    if not spanning.has_key(vx):
                        spanning[vx]=v
                    stack.append(vx)
            if children==0:
                leafs.append(v)
    rspan=dict()
    for key in spanning:
        if rspan.has_key(spanning[key]):
            rspan[spanning[key]].add(key)
        else:
            rspan[spanning[key]]={key,}
    return [spanning,leafs,rspan,root(spanning)]
def getchild(rspan,v):
    if rspan.has_key(v[0]):
        if v[1] in rspan[v[0]]:
            return [v[1],v[0]]
        else:
            return [v[0],v[1]]
    elif rspan.has_key(v[1]):
        if v[0] in rspan[v[1]]:
            return [v[0],v[1]]
        else:
            return [v[1],v[0]]
N=int(raw_input().strip()) 
lst=[int(i) for i in raw_input().strip().split(" ")]
total=0
for i in lst:
    total=total+i
edgelist=dict()
edges=list()
for i in range(N-1):
    (key,value)=(int(k) for k in raw_input().strip().split(" "))
    edges.append((key,value))
    if edgelist.has_key(key):
        edgelist[key].append(value)
    else:
        edgelist[key]=[value]
    if edgelist.has_key(value):
        edgelist[value].append(key)
    else:
        edgelist[value]=[key]
rs=dfs(edgelist,1)
leafs=rs[1]
spanningtree=rs[0]
rspan=rs[2]
croot=rs[3]
tlst=list(lst)

print "root==",
print croot
print "rspan=="

print rspan

children=True
cstack=list()
cstack.append(croot)
vst=[False]*len(lst)
while len(cstack)!=0:
    if not children:
        v=cstack.pop()
        if spanningtree.has_key(v):
            tlst[spanningtree[v]-1]=tlst[spanningtree[v]-1]+tlst[v-1]
        vst[v-1]=True
    else:
        v=cstack[-1]
    if rspan.has_key(v) and not vst[v-1]:
        for cv in rspan[v]:
            cstack.append(cv)
        children=True
    else:
        children=False
cnt=None
edg=None;
for edge in edges:
    [c,p]=getchild(rspan,edge)
   
    calk=total-tlst[c-1]
    cali=tlst[c-1]
    cal=0
    if cali>calk:
        cal=cali-calk
    else:
        cal=calk-cali
    if cnt==None:
        edg=[c,p]
        cnt=cal
    elif cnt>cal:
        edg=[c,p]
        cnt=cal
print cnt
