
import numpy as np
import pygame
import Heuristic
import State
import time

def terminal_state(board,s):
    # impl the case of H(n)
    endt=time.time()
    if(board.count('0') ==0) : return True   #need opt as string
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


def maximize(state,s,maxd):
    if(terminal_state(state.board,s)): return state.board,Heuristic.heuristic_scores(state.board,6,7)
    if state.d+1>maxd : return state.board,Heuristic.heuristic_scores(state.board,6,7) #call h(n)
    maxChild=None
    maxScore=-100000000000

    childs=child_creator(state)
    for child in childs:
        minch,score=minimize(child,s,maxd)
        if(score>maxScore) :
            maxChild=child
            maxScore=score
    return maxChild,maxScore

def minimize(state,s,maxd):
    if(terminal_state(state.board,s)): return state.board,Heuristic.heuristic_scores(state.board,6,7)
    if state.d + 1 > maxd: return state.board, Heuristic.heuristic_scores(state.board,6,7)
    minChild=None
    minScore=10000000000000

    childs=child_creator(state)
    for child in childs:
        minch,score=maximize(child,s,maxd)
        if(score<minScore) :
            minChild=child
            minScore=score
    return minChild,minScore

def changer(board, ind,val):
    returnedState=''
    returnedState += board[0:ind]
    returnedState += str(val)
    returnedState += board[ind+1:]
    return returnedState

def play(board):
    z=""
    for i in range(0, 7):
        for j in range(0, 6):
          z+=str(board[j, i])
    sta=State.State(z,None,0)
    md=5
    s=time.time()
    nstate,score=maximize(sta,s,md)
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
zz='111110000000000000000000000000000000000000'

a=np.zeros((7,6),int)
for i in range(0,7):
    for j in range(0,6):
        a[i,j]=int(zz[i*6+j])
        # print(state[i*6:i*6+6])
aa=np.copy(a.transpose())
print(np.flip(aa,axis=0))

xx=play(aa)
print(np.flip(xx,axis=0))
###################################run

# st=State.State(z,None,0)
# # ll=child_creator(z)
# # for tt in ll:
# #     print(tt.board)
# md=7
# s=time.time()
# l,m=maximize(st,s,md)
# ss=time.time()
# print(st.board)
# print(l.board)
# print(m)
# print(State.State.depth)
# print(ss-s)

###########################

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


