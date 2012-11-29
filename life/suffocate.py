#!/bin/python

# Head ends here

import random

class Grid(object):
    def __init__(self, player, cells):
        self.cells = cells
        self.grid_size = len(self.cells)
        self.player = player
        self.opponent = 'b' if player == 'w' else 'w'
        self.moves = []

    @property
    def population(self):
        return 29*29 - sum(row.count('-') for row in self.cells)

    def neighbors(self, i, j, matching='wb'):
        offsets = [
            (-1,-1), (0,-1), (1,-1),
            (-1,0),          (1,0),
            (-1,1),  (0,1),  (1,1),
        ]
        for a,b in offsets:
            x,y = i+a,j+b
            if x < 0 or x >= self.grid_size or y < 0 or y >= self.grid_size:
                continue
            if self.cells[x][y] in matching:
                yield (x,y)

    def neighbor_count(self, i, j, matching='wb'):
        return len(list(self.neighbors(i,j,matching)))

    def next_move(self):
        # search for opponent to suffocate
        for i in xrange(0,29):
            for j in xrange(0,29):
                if self.cells[i][j] != self.opponent:
                    continue

                if self.neighbor_count(i,j) <= 3:
                    for move in self.neighbors(i,j, matching='-'):
                        if self.neighbor_count(*move, matching='wb') <3:
                            return move

        i,j = 15,15
        while self.cells[i][j] != '-'
            i,j = random.randint(0,28), random.randint(0,28)
        return i,j







player = raw_input()[0]
board = []
for i in xrange(0, 29):
    board.append(raw_input()[:29])


grid = Grid(player, board)
a,b = grid.next_move()
print a,b