
import numpy as np
import pygame

import State
import time

def terminal_state(board,s):
    # impl the case of H(n)
    endt=time.time()
    if(np.count_nonzero(board) ==6*7) : return True
    # elif((endt-s)>10) :
    #     # print("#########################")
    #     # print(endt-s)
    #     # print(np.flip(board,axis=0))
    #     # print("#########################")
    #     return True
    else : return False

def assign(board, ind):
    returnedState=''
    returnedState += board[0:ind]
    returnedState += '1'
    returnedState += board[ind+1:]
    return returnedState


def get_valid_row(board, c):
	for r in range(0,6):
		if board[c*6+r] == '0':
			return c*6+r

def child_creator(state):
    childs=[]
    board=state.board
    for c in range(0,7):
        if(board[c*6+5]=='0'):
            cop=assign(board,get_valid_row(board,c))
            # cop[get_valid_row(board,c)]='1'
            newCh=State.State(cop,board,state.d+1)
            newCh.inc()
            # newCh = cop
            childs.append(newCh)
    return childs


def maximize(state,s,alpha,beta,maxd):
    if(terminal_state(state.board,s)): return None,state.evaluate()
    if state.d + 1 > maxd: return None, state.evaluate()

    maxChild=state
    maxScore=-1000000

    childs=child_creator(state)
    for child in childs:
        minch,score=minimize(child,s,alpha,beta,maxd)
        if(score>maxScore) :
            maxChild=child
            maxScore=score

        if(maxScore>=beta): break
        if(maxScore>alpha): alpha=maxScore
    return maxChild,maxScore

def minimize(state,s,alpha,beta,maxd):
    if(terminal_state(state.board,s)): return None,state.evaluate()
    if state.d + 1 > maxd: return None, state.evaluate()

    minChild=None
    minScore=10000000

    childs=child_creator(state)
    for child in childs:
        minch,score=maximize(child,s,alpha,beta,maxd)
        if(score<minScore) :
            minChild=child
            minScore=score

        if(minScore<=alpha): break
        if(minScore<beta): beta=minScore
    return minChild,minScore

def play(board):
    z=""
    for i in range(0, 7):
        for j in range(0, 6):
          z+=str(board[j, i])
    sta=State.State(z,None,0)
    md=5
    s=time.time()
    mm = 100000
    nstate,score=maximize(sta,s,-mm,mm,md)
    a = np.zeros((7, 6),int)
    for i in range(0, 7):
        for j in range(0, 6):
            a[i, j] = int(nstate.board[i * 6 + j])
    rboard = np.copy(a.transpose())
    print(np.flip(rboard,axis=0))
    return rboard

x=6
y=7
#z="100000100000100000100000100000100000100000"
#z="110000110000110000110000110000110000110000"
z="000000000000000000000000000000000000000000"
st=State.State(z,None,0)
# ll=child_creator(z)
# for tt in ll:
#     print(tt.board)

md=11
s=time.time()
mm=100000
l,m=maximize(st,s,-mm,mm,md)
ss=time.time()
print(st.board)
print(l.board)
print(m)
print(State.State.depth)
print(ss-s)

# z=np.zeros((6,7))
# x=3
# y=7
# for i in range(0,x):
#     for j in range(0,y):
#         z[i,j]=1
# st=State.State(z,None)
# temp=child_creator(z)
# for t in temp:
#     print(t.parent)

# print(terminal_state(z))

# s=time.time()
# l,m=maximize(st,s)
# print(np.flip(st.board,axis=0))
# print(np.flip(l.board,axis=0))
# print(m)


