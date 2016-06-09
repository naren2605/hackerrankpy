n=int(raw_input())
def ispal(s,i):
    found=False
    left=0
    right=len(s)-1
    while left<=right:
        if left==i:
            left+=1
        if right==i:
            right-=1
        if s[left]==s[right]:
            found=True
            left+=1
            right-=1
            continue
        else :
              return False
        break
    return found
def ispaln(s):
    found=False
    left=0
    right=len(s)-1
    while left<=right:
        if s[left]==s[right]:
            found=True
            left+=1
            right-=1
            continue
        else :
              return False
        break
    return found
for i in range(n):
    import time
    s=raw_input()
    found=-1
#    print time.ctime(),"isplan1"
    if ispaln(s):
        print(-1)
        continue
    lastchar=""
#    print time.ctime(),"isplan1e"
    for i in range(len(s)):
        
        if lastchar==s[i]:
            continue
        lastchar=s[i]
#        print time.ctime(),"isplani",i
        if(s[i]!=s[len(s)-1-i]):
            if ispal(s,i):
                found=i
                break
#        print time.ctime(),"isplanie",i,found
#    print time.ctime(),"======"
    print found
#    print time.ctime()
