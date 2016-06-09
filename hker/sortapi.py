def insertion_sort(l):
    icount=0
    for i in xrange(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
            l[j+1] = l[j]
            j -= 1
            icount+=1
        l[j+1] = key
    print icount

def insertion_analysis(l):
    icount=0
    for i in xrange(1, len(l)):
        j = i-1
        key = l[i]
        qsort(l,0,j)
        lc=0
        print l
        if key<=l[j]:
            continue
        j=0
        dup=0
        while (j<i):
            if l[j] > key:
                icount=icount+j+1
                break
            elif l[j]==key:
                dup = dup+1
            j += 1
        icount=icount-dup
        print icount
    return icount
global test
test=0
def swap(l,i,j):
    print test
    l[i],l[j]=l[j],l[i]

def lamuto_partition(l,lo,hi):
    pivot=l[hi]
    i=lo
    j=lo
    while j<=hi-1:
        if l[j]<=pivot:
            swap(l,i,j)
            i+=1
        j+=1
    swap(l,i,hi)
    return i

def qsort(l,lo,hi):
    if lo>=hi:
        return
    else:
        i=lamuto_partition(l,lo,hi)
        qsort(l,lo,i-1)
        qsort(l,i+1,hi)
