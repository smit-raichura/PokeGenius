from move_strategy import PichuMoveStrategy, PikachuMoveStrategy, RaichuMoveStrategy
from piece import Piece

class PieceFactory:
    @staticmethod
    def create_piece(piece_type):
        if piece_type == 'w' or piece_type == 'b':
            return Piece(PichuMoveStrategy())
        elif piece_type == 'W' or piece_type == 'B':
            return Piece(PikachuMoveStrategy())
        elif piece_type == '@' or piece_type == '$':
            return Piece(RaichuMoveStrategy())
        else:
            raise ValueError("Unknown piece type")

