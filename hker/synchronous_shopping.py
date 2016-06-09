import Queue
(N,M,K)=(int(i) for i in raw_input().strip().split(" "))
print N,
print M,
print K
shops=list()
for i in range(N):
	shops.append(tuple(int(i) for i in raw_input().strip().split(" ")))
print "shops:",
print shops
connections=list()
for i in range(M):
	connections.append(tuple(int(i) for i in raw_input().strip().split(" ")))
print "connections:",
print connections
edgelist=dict()
for i in connections:
	if edgelist.has_key(i[0]):
		edgelist[i[0]].append(i[1]);
		if edgelist.has_key(i[1]):
			edgelist[i[1]].append(i[0])
		else:
			edgelist[i[1]]=[i[0]]
	else:
		edgelist[i[0]]=[i[1]]
		if edgelist.has_key(i[1]):
			edgelist[i[1]].append(i[0])
		else:
			edgelist[i[1]]=[i[0]]
print "edgelist:",
print edgelist

def neighbours(edgelist,node):
        if edgelist.has_key(node):
                for i in edgelist[node]:
                        yield i
"""
implementation of bfs or implementation
of dikstra's with edge cost 1
"""
def bfs(edgelist,start,end=None):
        d=dict()
        q=Queue.PriorityQueue()
        q.put((start,0))
        d[start]=0
        spanning=dict()
        while not q.empty():
                e=q.get()
                for i in edgelist[e[0]]:
                        if d.has_key(i):
                                if d[i]>e[1]+1:
                                        spanning[i]=e[0]
                                        d[i]=e[1]+1
                                        q.put((i,e[1]+1))
                        else:
                                d[i]=e[1]+1
                                spanning[i]=e[0]
                                q.put((i,e[1]+1))
        print "spanning tree==> ",
        print spanning
bfs(edgelist,1)
