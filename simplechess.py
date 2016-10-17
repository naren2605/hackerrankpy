# Enter your code here. Read input from STDIN. Print output to STDOUT
g=int(raw_input())
(w,b,m)=(int(i) for i in raw_input().split(' '))
game=[]
for i in range(4):
    game.append([['',''],['',''],['',''],['','']])
def col(data):
    if data=='A':
        return 0
    elif data=='B':
        return 1
    elif data=='C':
        return 2
    elif data=='D':
        return 3
def valid(pr,pc):
    if (pr>=0 and pr<=3) and (pc>=0 and pc<=3):
        return True
    else:
        return False
def capture(pr,pc,ptype):
    r=pr
    c=pc
    emptycell=['','']
    if len(game[r][c])==2 and game[r][c][1]==ptype and game[r][c]!=emptycell:
        return -1
    elif len(game[r][c])==2 and game[r][c]!=emptycell:
        return 1
    else:
        return 0
def knight(position,ptype):
    moves=[]
    r=position[0]
    c=position[1]
    pr,pc=r-2,c+1
    if valid(pr,pc) and capture(pr,pc,ptype)!=-1:
        moves.append([pr,pc])
    pr,pc=r-1,c+2
    if valid(pr,pc) and capture(pr,pc,ptype)!=-1:
        moves.append([pr,pc])
    pr,pc=r-2,c-1
    if valid(pr,pc) and capture(pr,pc,ptype)!=-1:
        moves.append([pr,pc])
    pr,pc=r-1,c-2
    if valid(pr,pc) and capture(pr,pc,ptype)!=-1:
        moves.append([pr,pc])
    pr,pc=r+2,c-1
    if valid(pr,pc) and capture(pr,pc,ptype)!=-1:
        moves.append([pr,pc])
    pr,pc=r+2,c-2
    if valid(pr,pc) and capture(pr,pc,ptype)!=-1:
        moves.append([pr,pc])
    pr,pc=r+2,c+1
    if valid(pr,pc) and capture(pr,pc,ptype)!=-1:
        moves.append([pr,pc])
    pr,pc=r+2,c+2
    if valid(pr,pc) and capture(pr,pc,ptype)!=-1:
        moves.append([pr,pc])
    return moves
def queen(position,ptype):
    moves=bishop(position,ptype)+rook(position,ptype)
    return moves
def bishop(position,ptype):
    r,c=position[0],position[1]
    ri=r-1
    ci=c+1
    moves=[]
    while ri>=0 and ci<=3:
        if valid(ri,ci) and capture(ri,ci,ptype)!=-1:
            moves.append([ri,ci])
        else:
            break
        ri=ri-1
        ci=ci+1
    ri=r+1
    ci=c-1
    while ri<=3 and ci>=0:
        if valid(ri,ci) and capture(ri,ci,ptype)!=-1:
            moves.append([ri,ci])
        else:
            break
        ri=ri+1
        ci=ci-1
    ri=r-1
    ci=c-1
    while ri>=0 and ci>=0:
        if valid(ri,ci) and capture(ri,ci,ptype)!=-1:
            moves.append([ri,ci])
        else:
            break
        ri=ri-1
        ci=ci-1
    ri=r+1
    ci=c+1
    while ri<=3 and ci<=3:
        if valid(ri,ci) and capture(ri,ci,ptype)!=-1:
            moves.append([ri,ci])
        else:
            break
        ri=ri+1
        ci=ci+1
    return moves
def rook(position,ptype):
    r,c=position[0],position[1]
    moves=[]
    pc=c+1
    while pc<=3:
        if valid(r,pc) and capture(r,pc,ptype)!=-1:
            moves.append([r,pc])
        else:
            break
        pc=pc+1
    pc=c-1
    while pc>=0:
        if valid(r,pc) and capture(r,pc,ptype)!=-1:
            moves.append([r,pc])
        else:
            break
        pc=pc-1
    pr=r+1
    while pr<=3:
        if valid(pr,c) and capture(pr,c,ptype)!=-1:
            moves.append([pr,c])
        else:
            break
        pr=pr+1
    pr=r-1
    while pr>=0:
        if valid(pr,c) and capture(pr,c,ptype)!=-1:
            moves.append([pr,c]);
        else:
            break
        pr=pr-1
    return moves
def move(pawn,position,ptype):
    if pawn=='Q':
        return queen(position,ptype)
    elif pawn=='N1' or pawn=='N2':
        return knight(position,ptype)
    elif pawn=='B1' or pawn=='B2':
        return bishop(position,ptype)
    elif pawn=='R1' or pawn=='R2':
        return rook(position,ptype)
whites=[]
blacks=[]
cwhites=set()
cblacks=set()
for i in range(w+b):
    (piece,c,r)=(k for k in raw_input().split(' '))
    r=int(r)-1
    c=col(c)
    if i<w:
        if piece!='Q':
            if piece not in cwhites:
                cwhites.add(piece)
                piece=piece+'1'
            else:
                piece=piece+'2'
        game[r][c]=[piece,'W']
        whites.append([piece,'W',[r,c]])
    else:
        if piece!='Q':
            if piece not in cblacks:
                cblacks.add(piece)
                piece=piece+'1'
            else:
                piece=piece+'2'
        game[r][c]=[piece,'B']
        blacks.append([piece,'B',[r,c]])
#print "w---",whites
#print "b---",blacks
cwhites=set()
cblacks=set()
whites=[]
blacks=[]
def updategmedata():
    global whites
    global blacks
    whites=[]
    blacks=[]
    for ik in range(4):
        for jk in range(4):
            if game[ik][jk][1]=='W':
                whites.append([game[ik][jk][0],'W',[ik,jk]])
            elif game[ik][jk][1]=='B':
                blacks.append([game[ik][jk][0],'B',[ik,jk]])
    #print whites
    #print blacks
def printgame():
    for ki in range(4):
        for ji in range(4):
            pass
            #print game[ki][ji],":",
        #print
#printgame()
wkilled=set()
bkilled=set()
capturestack=[]
def playbrutechess(player,wmove,bmove,m):
    #print "player--->",player,wmove,bmove,m
    updategmedata()
    if wmove>m:
        return False
    if player=='W':
        for piece in whites:
            #print "piece--",piece
            if piece[0] not in wkilled:
                imoves=move(piece[0],piece[2],'W')
                for imove in imoves:
                    icapture=capture(imove[0],imove[1],'W')
                    if icapture==1:
                        capturedpiece=game[imove[0]][imove[1]][0]
                        #print piece[0]," at ",piece[2]," kills ",capturedpiece," at ",[imove[0],imove[1]]
                        if capturedpiece=='Q' and 'Q' in wkilled:
                            continue
                        elif capturedpiece=='Q':
                            return True
                        else:
                            bkilled.add(capturedpiece)
                            present_opp_pawn_loc=[imove[0],imove[1]]
                            future_opp_pawn_loc=[]
                            capturestack.append([present_opp_pawn_loc,future_opp_pawn_loc,capturedpiece,'B'])
                            present_own_pawn_loc=[piece[2][0],piece[2][1]]
                            future_own_pawn_loc=[imove[0],imove[1]]
                            game[imove[0]][imove[1]]=game[piece[2][0]][piece[2][1]]
                            game[piece[2][0]][piece[2][1]]=['','']
                            capturestack.append([present_own_pawn_loc,future_own_pawn_loc,piece[0],'W'])
                            #printgame()
                            flag=playbrutechess('B',wmove,bmove+1,m)
                            if flag:
                                return True
                            present=capturestack.pop()
                            future=capturestack.pop()
                            game[present[0][0],present[0][1]]=game[present[1][0],present[1][1]]
                            if future[0]==present[1] and future[3]!=present[3]:
                                #print "resetting the kill..."
                                game[present[1][0]][present[1][1]]=[future[2]][future[3]]
                                bkilled.remove(future[2])
                            else:
                                game[present[1][0]][present[1][1]]=game[future[0][0]][future[0][1]]                          
                    elif icapture==0:
                        nextmove=[imove[0],imove[1]]
                        present_own_pawn_loc=[piece[2][0],piece[2][1]]
                        game[imove[0]][imove[1]]=game[piece[2][0]][piece[2][1]]
                        game[piece[2][0]][piece[2][1]]=['','']
                        capturestack.append([present_own_pawn_loc,nextmove,piece[0],'W'])
                        #print piece[0],"moves from position",piece[2]," to ",nextmove
                        #printgame()
                        flag=playbrutechess('B',wmove,bmove+1,m)
                        if flag:
                            return True
                        present=capturestack.pop()
                        game[present[0][0]][present[0][1]]=game[present[1][0]][present[1][1]]
                        game[present[1][0]][present[1][1]]=['','']
    elif player=='B':
        for piece in blacks:
            if piece[0] not in bkilled:
                imoves=move(piece[0],piece[2],'B')
                for imove in imoves:
                    icapture=capture(imove[0],imove[1],'B')
                    if icapture==1:
                        capturedpiece=game[imove[0]][imove[1]][0]
                        #print piece[0]," at ",piece[2]," kills ",capturedpiece," at ",[imove[0],imove[1]]
                        if capturedpiece=='Q':
                            continue
                        else:
                            wkilled.add(capturedpiece)
                            present_opp_pawn_loc=[imove[0],imove[1]]
                            future_opp_pawn_loc=[]
                            capturestack.append([present_opp_pawn_loc,future_opp_pawn_loc,capturedpiece,'W'])
                            present_own_pawn_loc=[piece[2][0],piece[2][1]]
                            future_own_pawn_loc=[imove[0],imove[1]]
                            game[imove[0]][imove[1]]=game[piece[2][0]][piece[2][1]]
                            game[piece[2][0]][piece[2][1]]=['','']
                            capturestack.append([present_own_pawn_loc,future_own_pawn_loc,piece[0],'B'])
                            #printgame()
                            flag=playbrutechess('W',wmove+1,bmove,m)
                            if flag:
                                return True
                            present=capturestack.pop()
                            future=capturestack.pop()
                            game[present[0][0]][present[0][1]]=game[present[1][0]][present[1][1]]
                            if future[0]==present[1] and future[3]!=present[3]:
                                #print "resetting the kill..."
                                game[present[1][0]][present[1][1]]=[future[2],future[3]]
                                wkilled.remove(future[2])
                            else:
                                game[present[1][0]][present[1][1]]=game[future[0][0]][future[0][1]]                          
                    elif icapture==0:
                        nextmove=[imove[0],imove[1]]
                        present_own_pawn_loc=[piece[2][0],piece[2][1]]
                        game[imove[0]][imove[1]]=game[piece[2][0]][piece[2][1]]
                        game[piece[2][0]][piece[2][1]]=['','']
                        capturestack.append([present_own_pawn_loc,nextmove,piece[0],'B'])
                        #print piece[0],"moves from position",piece[2]," to ",nextmove
                        printgame()
                        flag=playbrutechess('W',wmove+1,bmove,m)
                        if flag:
                            return True
                        present=capturestack.pop()
                        game[present[0][0]][present[0][1]]=game[present[1][0]][present[1][1]]
                        game[present[1][0]][present[1][1]]=['','']
                
    return False
outcome=playbrutechess('W',1,0,m)
if outcome:
    print "YES"
else:
    print "NO"
