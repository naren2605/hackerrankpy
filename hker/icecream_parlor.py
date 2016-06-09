# Enter your code here. Read input from STDIN. Print output to STDOUT
import time
T=int(raw_input())
def binary_search(lst,key,lo,hi):
    lo=lo
    hi=hi
    while lo<=hi:
        mid=(hi+lo)/2
        if lst[mid]==key:
            return mid
        elif key>lst[mid]:
            lo=mid+1
        else:
            hi=mid-1
    return None
for i in range(T):
    M=int(raw_input())
    N=int(raw_input())
    lst=[int(i) for i in raw_input().strip().split(" ")]
    dl=dict()
    #print "1--- "+str(time.ctime())
    for li in range(len(lst)):
        if dl.has_key(lst[li]):
            dl[lst[li]].append(li)
        else:
            dl[lst[li]]=[li]
    #print dl
    lst.sort()
    if lst[0]>=M:
        continue
    length=len(lst)
    #print "2--- "+str(time.ctime())
    for li in range(length):
        index=-1
	if lst[li]<M:
            #print "4--4- "+str(time.ctime())+" "+str(M-lst[li])+":"+str(lst[li])
            index=binary_search(lst,M-lst[li],lo=(li+1),hi=length-1)
            #print index
	    #print "4--- "+str(time.ctime())
	else:
            break
        if index!=None and index!=-1:
            if lst[li]==M-lst[li] and len(dl[lst[index]])>1:
                nk=dl[lst[li]][0]+1
                kk=dl[lst[index]][1]+1
                if nk>kk:
                    print str(kk)+" "+str(nk)
                else:
                    print str(nk)+" "+str(kk)
            else:
                nk=dl[lst[li]][0]+1
                kk=dl[lst[index]][0]+1
                if nk>kk:
                    print str(kk)+" "+str(nk)
                else:
                    print str(nk)+" "+str(kk)
            break
#print list
