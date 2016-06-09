# Enter your code here. Read input from STDIN. Print output to STDOUT
print "change 2"
file=open("sherlock_test2.txt","r")
raw_input=file.next
comp=dict()
n=int(raw_input().strip())
def nP2(n):
    if n<2:
        return 0
    return n*(n-1)
for i in xrange(n):
    #l=int(raw_input().strip())
    raw_input()
    a=dict()
    total=0;
    for t in raw_input().split(' '):
        if not a.has_key(t):
            a[t]=1
        else:
            a[t]=a[t]+1
    print len(a.keys())

    for key in a:
        total=total+nP2(a[key]);
    print total
