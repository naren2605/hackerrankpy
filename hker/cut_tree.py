# Enter your code here. Read input from STDIN. Print output to STDOUT
visited=dict()
def getneighbours(edgelist,v):
    for key in edgelist[v]:
        yield key
def dfs(graph,start):
    count=0
    stack=list()
    stack.append(start)
    while len(stack)!=0:
        v=stack.pop()
        if not visited.has_key(v):
            count=count+lst[v-1]
            visited[v]=True
            for vx in getneighbours(graph,v):
                if not visited.has_key(vx):
                    stack.append(vx)
    return count
N=int(raw_input().strip().split(" ")) 
lst=[int(i) for i in raw_input().strip().split(" ")]
total=0
for i in lst:
    total=total+i
edgelist=dict()
edges=list()
for i in range(N):
    (key,value)=(int(k) for k in raw_input().strip().split(" "))
    edges.append((key,value))
    if edgelist.has_key(key):
        edgelist[key].append(value)
    else:
        edgelist[key]=[value]
print dfs(edgelist,1)