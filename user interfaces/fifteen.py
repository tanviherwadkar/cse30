# assignment: programming assignment 5: fifteen puzzle
# author: Tanvi Herwadkar
# date: December 2, 2022
# file: fifteen.py implements an ascii version of the fifteen game
# input: tile to swap with the empty space
# output: board with swapped tiles
# methods: draw(): draws board
#          makestring(): converts numbers to printable string
#          transpose(): switches elements
#          shuffle(): shuffles board
### EC:    is_solvable(): determines wether or not this permutation is solvable
from random import *
from copy import deepcopy
from queue import Queue

class Fifteen:

    # create a vector (ndarray) of tiles and the layout of tiles positions (a graph)
    # tiles are numbered 1-15, the last tile is 0 (an empty space)
    def __init__(self, size=4): 
        self.goal = {1: ' 1 ', 2: ' 2 ', 3: ' 3 ', 4: ' 4 ', 5: ' 5 ', 6: ' 6 ', 7: ' 7 ', 8: ' 8 ', 9: ' 9 ', 10: '10 ', 11: '11 ', 12: '12 ', 13: '13 ', 14: '14 ', 15: '15 ', 16: '   '}
        self.tiles = {}
        self.position = 16
        for i in range(1, 17):
            self.tiles[i] = self.format(str(i))
        self.UP = 0
        self.RIGHT = 1
        self.DOWN = 2
        self.LEFT = 3

    # draw the layout with tiles:
    # +---+---+---+---+
    # | 1 | 2 | 3 | 4 |
    # +---+---+---+---+
    # | 5 | 6 | 7 | 8 |
    # +---+---+---+---+
    # | 9 |10 |11 |12 |
    # +---+---+---+---+
    # |13 |14 |15 |   |
    # +---+---+---+---+
    def draw(self):
        d = self.tiles
        print('+---+---+---+---+')
        print(f"|{d[1]}|{d[2]}|{d[3]}|{d[4]}|")
        print('+---+---+---+---+')
        print(f"|{d[5]}|{d[6]}|{d[7]}|{d[8]}|")
        print('+---+---+---+---+')
        print(f"|{d[9]}|{d[10]}|{d[11]}|{d[12]}|")
        print('+---+---+---+---+')
        print(f"|{d[13]}|{d[14]}|{d[15]}|{d[16]}|")
        print('+---+---+---+---+')

    def format(self, ch):
        ch = ch.strip()
        if len(ch) == 1:
            return ' ' + ch + ' '
        elif ch == '16':
            return '   '
        elif len(ch) == 2:
            return ch + ' '

    # return a string representation of the vector of tiles as a 2d array  
    # 1  2  3  4
    # 5  6  7  8
    # 9 10 11 12
    #13 14 15 
    def __str__(self):
        d = self.tiles
        return f"{d[1]}{d[2]}{d[3]}{d[4]}\n{d[5]}{d[6]}{d[7]}{d[8]}\n{d[9]}{d[10]}{d[11]}{d[12]}\n{d[13]}{d[14]}{d[15]}{d[16]}\n"

    # exchange i-tile with j-tile  
    # tiles are numbered 1-15, the last tile is 0 (empty space) 
    # the exchange can be done using a dot product (not required)
    # can return the dot product (not required)
    def transpose(self, i, j): 
        i = self.position
        if not self.is_valid_move(j):
            return False
        for a, b in self.tiles.items():
            if b == self.format(str(j)):
                j = a
                break
        self.tiles[i], self.tiles[j] = self.tiles[j], self.tiles[i]
        self.position = j
        return "All Good!"

    def get_row_col(self, value):
        row = (value - 1) // 4
        col = (value - 1) % 4
        return row, col

    def get_tile(self, row, col):
        pos = (row * 4) + (col) + 1
        return pos, self.tiles[pos], self.tiles

    def up(self, value):
        row, col = self.get_row_col(value)
        if row > 0:
            row -= 1
        return self.get_tile(row, col)

    def right(self, value):
        row, col = self.get_row_col(value)
        if col < 3:
            col += 1
        return self.get_tile(row, col)

    def down(self, value):
        row, col = self.get_row_col(value)
        if row < 3:
            row += 1
        return self.get_tile(row, col)

    def left(self, value):
        row, col = self.get_row_col(value)
        if col > 0:
            col -= 1
        return self.get_tile(row, col)

    def search_and_swap(self, value):
        choices = [self.up(value), self.right(value), self.down(value), self.left(value)]
        space = self.position
        for pos, _, _ in choices:
            if pos == space:
                self.tiles[space], self.tiles[value] = self.tiles[value], self.tiles[space]
                self.position = value
                return True
        return False

    def swap(self, pos, space, tiles):
        if pos != space:
            tiles[space], tiles[pos] = tiles[pos], tiles[space]
        return pos

    def next_moves(self, board, space):
        next_space = [space, space, space, space]
        next_board = [deepcopy(board), deepcopy(board), deepcopy(board), deepcopy(board)]

        pos, _, _ = self.up(space)
        next_space[self.UP] = self.swap(pos, space, next_board[self.UP])
        # print(f"Up: {space}, {next_space[self.UP]}, {next_board[self.UP]}")

        pos, _, _ = self.right(space)
        next_space[self.RIGHT] = self.swap(pos, space, next_board[self.RIGHT])
        # print(f"Right: {space}, {next_space[self.RIGHT]}, {next_board[self.RIGHT]}")

        pos, _, _ = self.down(space)
        next_space[self.DOWN] = self.swap(pos, space, next_board[self.DOWN])
        # print(f"Down: {space}, {next_space[self.DOWN]}, {next_board[self.DOWN]}")

        pos, _, _ = self.left(space)
        next_space[self.LEFT] = self.swap(pos, space, next_board[self.LEFT])
        # print(f"Left: {space}, {next_space[self.LEFT]}, {next_board[self.LEFT]}")

        return [[next_board[self.UP], next_space[self.UP], self.UP], 
                [next_board[self.RIGHT], next_space[self.RIGHT], self.RIGHT],
                [next_board[self.DOWN], next_space[self.DOWN], self.DOWN],
                [next_board[self.LEFT], next_space[self.LEFT], self.LEFT]]

    # solve the puzzle (optional)
    def solve(self):
        # initialize BFS search
        bfs_done = []
        bfs_suggest = Queue()
        # init BFS search with initial board configuration
        bfs_suggest.put({"board": self.tiles, "space": self.position, "solution": []})

        # search tree
        while True:
            # quit if no solution was found
            if bfs_suggest.empty():
                print("Game Not Solved.")
                return []

            # dequeue and investigate current BFS choice
            node = bfs_suggest.get()

            # quit if the current board is our goal
            if node["board"] == self.goal:
                print("Game Solved.")
                return node["solution"]

            # add current board to suggestions we have already examined, and
            # add its child boards to our BFS suggestions
            if node["board"] not in bfs_done:
                bfs_done.append(node["board"])
                for move in self.next_moves(node["board"], node["space"]):
                    if move[0] not in bfs_done:
                        bfs_suggest.put({"board": move[0], "space": move[1], "solution": node["solution"] + [move[2]]})

    # checks if the move is valid: one of the tiles is 0 and another tile is its neighbor 
    def is_valid_move(self, move):
        strmove = self.format(str(move))
        allmoves = self.valid_moves()
        if strmove in allmoves:
            return True
        return False

    def valid_moves(self):
        pos = self.position
        # pos+1 pos+4
        if pos == 1:
            return [self.tiles[pos+1], self.tiles[pos+4]]
        
        # pos+1 pos+4 pos-1
        if pos == 2 or pos == 3:
            return [self.tiles[pos+1], self.tiles[pos+4], self.tiles[pos-1]]

        #pos-1 pos+4
        if pos == 4:
            return [self.tiles[pos+4], self.tiles[pos-1]]

        #pos+1 pos-4 pos+4
        if pos == 5 or pos == 9:
            return [self.tiles[pos+4], self.tiles[pos+1], self.tiles[pos-4]]

        #pos+1 pos-1 pos-4 pos+4
        if pos in [6, 7, 10, 11]:
            return [self.tiles[pos+4], self.tiles[pos-1], self.tiles[pos-4], self.tiles[pos+1]]
        
        #pos-1 pos-4 pos+4
        if pos == 8 or pos == 12:
            return [self.tiles[pos+4], self.tiles[pos-1], self.tiles[pos-4]]

        #pos+1 pos-4
        if pos == 13:
            return [self.tiles[pos+1], self.tiles[pos-4]]

        #pos+1 pos-1 pos-4
        if pos == 14 or pos == 15:
            return [self.tiles[pos+1], self.tiles[pos-4], self.tiles[pos-1]]

        #pos-1 pos-4
        if pos == 16:
            return [self.tiles[pos-4], self.tiles[pos-1]]

    # update the vector of tiles
    # if the move is valid assign the vector to the return of transpose() or call transpose 
    def update(self, move):
        if not self.is_valid_move(move):
            return False
        j = move
        i = self.position
        for a, b in self.tiles.items():
            if b == self.format(str(j)):
                j = a
                break
        self.tiles[i], self.tiles[j] = self.tiles[j], self.tiles[i]
        self.position = j
    
    # shuffle tiles
    def shuffle(self, moves = 10):
        for _ in range(moves):
            lst = self.valid_moves()
            lst1 = []
            for j in lst:
                lst1.append(int(j.strip()))
            self.transpose("x", lst1[randint(0, len(lst1)-1)])
    
    # verify if the puzzle is solved
    def is_solved(self):
        if self.tiles == self.goal:
            return True
        return False

    def get_items(self):
        return self.tiles

    # get the permutation of tile values
    def get_tile_permutation(self):
        permutation = []
        for key, value in self.get_items().items():
            value = value.strip()
            if value == "":
                continue
            permutation.append(int(value))
        return permutation

    # verify if the puzzle is solvable (optional)
    def is_solvable(self):
        inversions = 0
        permutation = self.get_tile_permutation()
        for i in range(len(permutation)):
            for j in range(i+1, len(permutation)):
                if permutation[i] > permutation[j]:
                    inversions += 1
        if inversions % 2 == 0:
            print(f"{permutation} is solvable.")
            return True
        else:
            print(f"{permutation} is not solvable.")
            return False

if __name__ == '__main__':
    game = Fifteen()
    game.shuffle()
    game.is_solvable()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        x = game.transpose("x", int(move))
        if x == False:
            continue
        game.draw()
        if game.is_solved():
            break
    print('Game over!')