import copy

def board_to_matrix(board, N):
    temp = [board[i: i + N] for i in range(0, len(board), N)]
    return [list(ele) for ele in temp]

def toString(board, N):
    stringBoard = [y for x in board for y in x]
    return ''.join(stringBoard)

def board_to_string(board, N):
    return "\n".join(board[i:i+N] for i in range(0, len(board), N))

def is_within_bounds(N, r, c):
    return 0 <= r < N and 0 <= c < N

def move_piece(board, src, dest):
    new_board = copy.deepcopy(board)
    new_board[dest[0]][dest[1]] = new_board[src[0]][src[1]]
    new_board[src[0]][src[1]] = '.'
    return new_board

def capture_piece(board, src, dest, capture_pos):
    new_board = move_piece(board, src, dest)
    new_board[capture_pos[0]][capture_pos[1]] = '.'
    return new_board

def get_piece_teams():
    team1 = ['w', 'W', '@']
    team2 = ['b', 'B', '$']
    return team1, team2

def get_positions(board, piece):
    return [(r, c) for r in range(len(board)) for c in range(len(board[r])) if board[r][c] == piece]

def evaluate_board(board, N):
    cost_dict = {
        '@': 20,
        'W': 7,
        'w': 3,
        '$': 20,
        'B': 7,
        'b': 3
    }
    w_val = 0
    b_val = 0
    for piece in ["w", "W", "@"]:
        w_val += len(get_positions(board, piece)) * cost_dict[piece]

    for piece in ["b", "B", "$"]:
        b_val -= len(get_positions(board, piece)) * cost_dict[piece]

    if w_val == 0 and b_val > 0:
        return float('-inf')
    elif b_val == 0 and w_val > 0:
        return float('inf')

    return w_val + b_val
