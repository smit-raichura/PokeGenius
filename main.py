import sys
from piece_factory import PieceFactory
from move_command import MoveCommand
from board_utils import board_to_matrix, toString, board_to_string, evaluate_board, get_positions

def find_best_move(board, N, player, timelimit):
    board = board_to_matrix(board, N)
    best_move = None

    pieces = ['w', 'W', '@'] if player in 'wW@' else ['b', 'B', '$']
    for piece in pieces:
        positions = get_positions(board, piece)
        for r, c in positions:
            piece_instance = PieceFactory.create_piece(piece)
            moves = piece_instance.get_valid_moves(board, N, r, c, player)
            for move in moves:
                command = MoveCommand(board, (r, c), move)
                new_board = command.execute()
                if not best_move or evaluate_board(new_board, N) > evaluate_board(best_move, N):
                    best_move = new_board

    return toString(best_move, N)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        raise Exception("Usage: Raichu.py N player board timelimit")

    (_, N, player, board, timelimit) = sys.argv
    N = int(N)
    timelimit = int(timelimit)
    if player not in "wb":
        raise Exception("Invalid player.")

    if len(board) != N * N or 0 in [c in "wb.WB@$" for c in board]:
        raise Exception("Bad board string.")

    print("Searching for best move for " + player + " from board state: \n" + board_to_string(board, N))
    print("Here's what I decided:")
    best_move = find_best_move(board, N, player, timelimit)
    print(best_move)
