# Enter your code here. Read input from STDIN. Print output to STDOUT
## hackerrank dfs-search -- cut the tree -- solution working
visited=dict()
def getneighbours(edgelist,v,lst):
    if edgelist.has_key(v[0]):
        for key in edgelist[v[0]]:
            yield (key,lst[key-1])
def root(span):
    r=None
    for key in span:
        r=key
        break
    while span.has_key(r):
        r=span[r]
    return r
def dfs(graph,start,lst):
    count=0
    stack=list()
    stack.append((start,lst[start-1]))
    spanning=dict()
    leafs=list()
    while len(stack)!=0:
        v=stack.pop()
        if not visited.has_key(v[0]):
            count=count+v[1]
            visited[v]=True
            children=0
            for vx in getneighbours(graph,v,lst):
                if not visited.has_key(vx):
                    children=children+1
                    if not spanning.has_key(vx):
                        spanning[vx]=v
                    stack.append(vx)
    rspan=dict()
    for key in spanning:
        if rspan.has_key(spanning[key]):
            rspan[spanning[key]].add(key)
        else:
            rspan[spanning[key]]={key,}
    #print rspan
    return [spanning,rspan,root(spanning)]
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
rs=dfs(edgelist,1,lst)

def postorder(tree,node):
    if not tree.has_key(node):
        return
    else:
        for child in tree[node]:
            postorder(tree,child);
            #print child,
spanning_tree=rs[0]
rspan=rs[1]
root=rs[2]
tstack=list()
tlst=list(lst)
tstack.append(root)
prev=None
#print "====post order===="
cnt=None
while len(tstack)!=0:
     v=tstack[-1]
     if not rspan.has_key(v): 
         v=tstack.pop()
         tlst[spanning_tree[v][0]-1]=tlst[spanning_tree[v][0]-1]+tlst[v[0]-1]
         tmpcount=total-tlst[v[0]-1]
         #print "tmpcount==",
         #print tmpcount,
         #print "vertex==",
         #print v
         if tmpcount>tlst[v[0]-1]:
             amt=tmpcount-tlst[v[0]-1]
             if cnt==None:
                 cnt=amt
             elif cnt>amt:
                 cnt=amt
         else:
             amt=tlst[v[0]-1]-tmpcount
             if cnt==None:
                 cnt=amt
             elif cnt>amt:
                 cnt=amt
         #print v,
     else:
         if prev in rspan[v]:
             v=tstack.pop()
             if v in spanning_tree:
                 tlst[spanning_tree[v][0]-1]=tlst[spanning_tree[v][0]-1]+tlst[v[0]-1]
             tmpcount=total-tlst[v[0]-1]
             #print "tmpcount==",
             #print tmpcount,
             #print "vertex==",
             #print v
             if tmpcount>tlst[v[0]-1]:
                amt=tmpcount-tlst[v[0]-1]
                if cnt==None:
                    cnt=amt
                elif cnt>amt:
                    cnt=amt
             else:
                 amt=tlst[v[0]-1]-tmpcount
                 if cnt==None:
                     cnt=amt
                 elif cnt>amt:
                     cnt=amt
             #print v,
         else:
             ltmp=[]
             for child in rspan[v]:
                 ltmp.append(child)
             while len(ltmp)!=0:
                 tstack.append(ltmp.pop())
     prev=v
print cnt
