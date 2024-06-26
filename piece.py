class Piece:
    def __init__(self, move_strategy):
        self.move_strategy = move_strategy

    def get_valid_moves(self, board, N, r, c, player):
        return self.move_strategy.get_valid_moves(board, N, r, c, player)

