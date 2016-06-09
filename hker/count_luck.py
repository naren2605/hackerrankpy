# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
def getneighbours(graph,vertex):
    cc=len(graph[0])
    rc=len(graph)
    if 0<=vertex[1]+1<cc and graph[vertex[0]][vertex[1]+1]!='X' and graph[vertex[0]][vertex[1]+1]!='M':
        yield [vertex[0],vertex[1]+1]
    if 0<=vertex[0]+1<rc and graph[vertex[0]+1][vertex[1]]!='X' and graph[vertex[0]+1][vertex[1]]!='M':
        yield [vertex[0]+1,vertex[1]]
    if 0<=vertex[1]-1<cc and graph[vertex[0]][vertex[1]-1]!='X' and graph[vertex[0]][vertex[1]-1]!='M':
        yield [vertex[0],vertex[1]-1]
    if 0<=vertex[0]-1<rc and graph[vertex[0]-1][vertex[1]]!='X' and graph[vertex[0]-1][vertex[1]]!='M':
        yield [vertex[0]-1,vertex[1]]
visited=dict()
def dfs(graph,vertex):
    count=0
    stack=list()
    path=dict()
    stack.append(vertex)
    found=None
    while len(stack)!=0:
        v=stack.pop()
        if not visited.has_key(tuple(v)):
            if graph[v[0]][v[1]]=='*':
                found=tuple(v)
                break
            visited[tuple(v)]=True
            for vx in getneighbours(graph,v):
                if not visited.has_key(tuple(vx)):
                    ##creating the spanning tree to back track
                    path[tuple(vx)]=tuple(v)
                    stack.append(vx)
                    
    spath=list()
    while path.has_key(found) and found!=None:
        spath.append(found)
        found=path[found]
    spath.append(tuple(vertex))
    revpath=dict()
    for key in path:
        if revpath.has_key(path[key]):
            revpath[path[key]].append(key)
        else:
            revpath[path[key]]=[key]
    if len(spath)>2:
        for i in spath:
            if revpath.has_key(i) and len(revpath[i])>1:
                count=count+1
    else:
        count=1
        
    return count
T=int(raw_input())
visited=dict()
for ti in range(T):
    (N,M)=(int(i) for i in raw_input().strip().split(" "))
    matrix=list()
    for i in range(N):
        matrix.append([k for k in raw_input().strip()]);
    K=int(raw_input())
    ktemp=None
    for i in range(N):
        for ik in range(M):
            if matrix[i][ik]=='M':
                ktemp=dfs(matrix,[i,ik])
                break
        if ktemp!=None:
            break
    if K==ktemp:
        print "Impressed"
    else:
        print "Oops!"
    visited=dict()
