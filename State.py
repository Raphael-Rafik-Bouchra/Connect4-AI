import numpy as np

class State:
    depth = 0
    def __init__(self, board,parent,d):
        self.board=board
        self.parent=parent
        self.d=d

    def evaluate(self):
        return np.random.randint(3,22)
    def inc(self):
        if(self.d>State.depth):State.depth=self.d
