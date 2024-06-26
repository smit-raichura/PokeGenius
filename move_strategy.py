from board_utils import is_within_bounds, move_piece, capture_piece, get_piece_teams

class MoveStrategy:
    def get_valid_moves(self, board, N, r, c, player):
        raise NotImplementedError

class PichuMoveStrategy(MoveStrategy):
    def get_valid_moves(self, board, N, r, c, player):
        team1, team2 = get_piece_teams()
        team = team1 if player in team1 else team2
        opponent = team2 if player in team1 else team1
        moves = []

        directions = [(-1, -1), (-1, 1)] if player == 'b' else [(1, -1), (1, 1)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if is_within_bounds(N, nr, nc):
                if board[nr][nc] == '.':
                    moves.append((nr, nc))
                elif board[nr][nc] in opponent:
                    jump_r, jump_c = nr + dr, nc + dc
                    if is_within_bounds(N, jump_r, jump_c) and board[jump_r][jump_c] == '.':
                        moves.append((jump_r, jump_c))

        return moves

class PikachuMoveStrategy(MoveStrategy):
    def get_valid_moves(self, board, N, r, c, player):
        team1, team2 = get_piece_teams()
        team = team1 if player in team1 else team2
        opponent = team2 if player in team1 else team1
        moves = []

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            for step in range(1, 3):
                nr, nc = r + dr * step, c + dc * step
                if is_within_bounds(N, nr, nc):
                    if board[nr][nc] == '.':
                        moves.append((nr, nc))
                    elif board[nr][nc] in opponent:
                        jump_r, jump_c = nr + dr, nc + dc
                        if is_within_bounds(N, jump_r, jump_c) and board[jump_r][jump_c] == '.':
                            moves.append((jump_r, jump_c))
                        break
                    else:
                        break
                else:
                    break

        return moves

class RaichuMoveStrategy(MoveStrategy):
    def get_valid_moves(self, board, N, r, c, player):
        team1, team2 = get_piece_teams()
        team = team1 if player in team1 else team2
        opponent = team2 if player in team1 else team1
        moves = []

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            while is_within_bounds(N, nr, nc):
                if board[nr][nc] == '.':
                    moves.append((nr, nc))
                elif board[nr][nc] in opponent:
                    jump_r, jump_c = nr + dr, nc + dc
                    if is_within_bounds(N, jump_r, jump_c) and board[jump_r][jump_c] == '.':
                        moves.append((jump_r, jump_c))
                    break
                else:
                    break
                nr, nc += dr, dc

        return moves

