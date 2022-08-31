# --------------------------- GLOBAL VARIABLES -----------------------------
import numpy as np

rows, cols = (6, 7)  # Initialized length and width of game board

AI = 1
Player = 2
none = 0

state = "000000" \
        "000000" \
        "000000" \
        "111111" \
        "222222" \
        "000000" \
        "000000"
place = "223322234432346643457754346642234432223322"

# ---------------------------------------------------------------------------

def scores(str, rows, cols, turn):
    total_score = 0
    if turn == 1:
        fors = '1111'
    else:
        fors = '2222'
    # Row
    for i in range(0, rows):
        lst = ''
        for j in range(0, cols):
            lst += (str[i + (j * rows)])
        for c in range(0, len(lst) - 3):
            total_score += lst.count(fors, i, 4 + c)
    # Column
    for i in range(0, int(len(str) / rows)):
        lst = str[rows * i:rows * (i + 1)]
        for c in range(0, len(lst) - 3):
            total_score += lst.count(fors, i, 4 + c)
    # Positive Diagonal
    for i in range(0, int(rows / 2)):
        lst = ''
        lst2 = ''
        for j in range(0, rows - i):
            lst += str[cols * j + i]
            lst2 += str[cols * (j + 1) - 1 + rows * i]
            for c in range(0, len(lst) - 3):
                total_score += (lst.count(fors, i, 4 + c) + lst2.count(fors, i, 4 + c))
    # Negative Diagonal
    Tstate = reverse_columns(str, cols, rows)
    for i in range(0, int(rows / 2)):
        lst = ''
        lst2 = ''
        for j in range(0, rows - i):
            lst += Tstate[cols * j + i]
            lst2 += Tstate[cols * (j + 1) - 1 + rows * i]
            for c in range(0, len(lst) - 3):
                total_score += (lst.count(fors, i, 4 + c) + lst2.count(fors, i, 4 + c))
    return total_score


# ---------------------------------------------------------------------------

def reverse_columns(str, cols, rows):
    Tstate = ''
    ind = cols - 1
    for i in range(cols):
        Tstate += str[ind * rows:(ind + 1) * rows]
        ind = ind - 1
    return Tstate


# ----------------------- HEURISTIC FUNCTIONS ------------------------------

def heuristic_scores(str, rows, cols):
    Tstate = reverse_columns(str, cols, rows)
    totalAI = 100 * scores(str, rows, cols, 1) + \
              get_rows_heuristic(str, rows, cols, 1,place) + \
              get_columns_heuristic(str, rows, 1,place) + \
              get_pos_diag_heuristic(str, rows, cols, 1,place) + \
              get_pos_diag_heuristic(Tstate, rows, cols, 1,place)
    totalHuman = 100 * scores(str, rows, cols, 2) + \
                 get_rows_heuristic(str, rows, cols, 2,place) + \
                 get_columns_heuristic(str, rows, 2,place) + \
                 get_pos_diag_heuristic(str, rows, cols, 2,place) + \
                 get_pos_diag_heuristic(Tstate, rows, cols, 2,place)
    return totalAI - totalHuman


def get_columns_heuristic(str, rows, turn, place):
    total_score = 0
    for i in range(int(len(str) / rows)):
        lst = str[rows * i:rows * (i + 1)]
        plc = place[rows * i:rows * (i + 1)]
        total_score += calculate(lst, turn, plc)
    return total_score


def get_rows_heuristic(str, rows, cols, turn,place):
    total_score = 0
    for i in range(rows):
        lst = ''
        plc = ''
        for j in range(cols):
            lst += (str[i + (j * rows)])
            plc += (place[i + (j * rows)])
        total_score += calculate(lst, turn,plc)
    return total_score


def get_pos_diag_heuristic(str, rows, cols, turn,place):
    total_score = 0
    for i in range(int(rows / 2)):
        lst = ''
        lst2 = ''
        plc = ''
        plc2 = ''
        for j in range(rows - i):
            lst += str[cols * j + i]
            plc += place[cols * j + i]
            lst2 += str[cols * (j + 1) - 1 + rows * i]
            plc2 += place[cols * (j + 1) - 1 + rows * i]
        total_score += (calculate(lst, turn,plc) + calculate(lst2, turn,plc2))
    return total_score


def calculate(row, turn, plc):
    flag = 0
    rsum = 0
    if turn == 1:
        fours = '1111'
        ones = '1'
        against = '2'
    else:
        fours = '2222'
        ones = '2'
        against = '1'
    for i in range(0, len(row) - 3):  # 11111    11110111
        if row[i:i + 4] == fours:
            if (flag == 0):
                rsum += (6 + int(plc[i]) + int(plc[i+1])+  int(plc[i+2])+ int(plc[i+3]) )
                flag = 1
            else:
                rsum += (5 + int(plc[i]) + int(plc[i+1])+  int(plc[i+2])+ int(plc[i+3]) )
        else:
            flag = 0
            f = 0
            oneSum = 0
            for j in range(i, i + 4):
                if (row[j] == ones):
                    oneSum += 1
                elif (row[j] == against):
                    oneSum = 0
                    f = 1
                    break
            if oneSum == 3:
                rsum += (3 + int(plc[i]) + int(plc[i+1])+  int(plc[i+2]))
                continue
            if oneSum == 2: rsum += (1 + int(plc[i]) + int(plc[i+1]))
    return rsum


# ---------TEST-------------

a = np.zeros((cols, rows))
for i in range(0, cols):
    for j in range(0, rows):
        a[i, j] = int(state[i * rows + j])
aa = a.transpose()
print(np.flip(aa, axis=0))
print(heuristic_scores(state, rows, cols))

# Tstate = reverse_columns(state,cols,rows)
#
# Cscore = get_columns_heuristic(state,rows,1)
# print("The Column score is:", Cscore)
# Rscore = get_rows_heuristic(state,rows,cols,1)
# print("The Row score is:", Rscore)
# PDscore = get_pos_diag_heuristic(state,rows,cols,1)
# print("The Positive Diagonal score is:", PDscore)
# NDscore = get_pos_diag_heuristic(Tstate,rows,cols,1)
# print("The Negative Diagonal score is:", NDscore)


# #4->6   3->3   2->1
# ar='0101011' #6
# arr='1101100' #8
# arrr='1100111' # 6
# ar4="1111111" #12
# aa='1111000' #10
# a1='1121110' #0
# #calcRow(a1)
#
# c1='112110' #0
# c2='111000' #4
# c3='212111' #0
# c4='111110' #14
# c5='111111' #16
# c6='211112' #6
# c7='111100' #10
# calcRow(c1)
