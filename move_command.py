import copy

class MoveCommand:
    def __init__(self, board, src, dest):
        self.board = board
        self.src = src
        self.dest = dest

    def execute(self):
        new_board = copy.deepcopy(self.board)
        new_board[self.dest[0]][self.dest[1]] = new_board[self.src[0]][self.src[1]]
        new_board[self.src[0]][self.src[1]] = '.'
        return new_board

