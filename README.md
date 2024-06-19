# PokeGenius

This project implements a game AI for Raichu, a variant of the classic strategy game where players use pieces named Pichu, Pikachu, and Raichu. The AI uses advanced algorithms to determine the best moves for a given game state.

## Table of Contents
- [Introduction](#introduction)
- [Game Rules](#game-rules)
- [Algorithm](#algorithm)
- [Setup](#setup)
- [Usage](#usage)


## Introduction

The Raichu Game AI project aims to create a competitive AI that can play Raichu effectively. The AI uses strategies and algorithms to evaluate and select the best possible moves given the current state of the game board.

## Game Rules

1. **Pieces**:
   - **Pichu**: Moves one step diagonally forward to an empty square.
   - **Pikachu**: Moves one or two steps forward, left, or right to an empty square.
   - **Raichu**: Moves like a queen in chess - any number of squares forward, backward, left, right, or diagonally to an empty square.

2. **Jumping and Capturing**:
   - **Pichu**: Can jump over an opponent's Pichu to capture it.
   - **Pikachu**: Can jump over an opponent's Pichu or Pikachu to capture it.
   - **Raichu**: Can jump over any opponent's piece to capture it.

3. **Promotion**:
   - When a Pichu or Pikachu reaches the opposite side of the board, it is promoted to a Raichu.

4. **Winning**:
   - The game is won by the player who captures all the opponent's pieces.

## Algorithm

The AI uses a combination of the following algorithms to determine the next best move:

## Minimax Algorithm

The Minimax algorithm is used to simulate all possible moves up to a certain depth, evaluating the board at each terminal state. The AI tries to maximize its score while minimizing the opponent's score.

### How Minimax Works

1. **Simulation**:
   - The algorithm simulates all possible moves for the current player.
   - For each move, it then simulates the opponent's possible responses.

2. **Depth**:
   - This process continues up to a certain depth (number of moves ahead).

3. **Evaluation**:
   - At each terminal state (leaf node of the tree), the algorithm evaluates the board using a scoring function.

4. **Decision Making**:
   - The AI chooses the move that maximizes its minimum gain (hence "minimax").

## Alpha-Beta Pruning

Alpha-Beta pruning is an optimization technique for the Minimax algorithm. It reduces the number of nodes evaluated in the game tree by eliminating branches that won't affect the final decision.

### How Alpha-Beta Pruning Works

1. **Alpha and Beta Values**:
   - Alpha represents the maximum score that the maximizing player is assured of.
   - Beta represents the minimum score that the minimizing player is assured of.

2. **Pruning**:
   - During the Minimax process, branches of the game tree that can't possibly influence the final decision are pruned (eliminated).

3. **Efficiency**:
   - This significantly improves the efficiency of the Minimax algorithm, allowing it to look further ahead in the game tree within the same time constraints.

## Evaluation Function

The evaluation function assesses the board state by assigning scores to the pieces based on their type and position:

```python
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
```
## How the Evaluation Function Works

### Scoring Pieces:

- Each piece type is assigned a score (e.g., Raichu = 20, Pikachu = 7, Pichu = 3).
- The function counts the number of each piece type on the board and multiplies by its score.

### Summing Scores:

- Scores for the current player's pieces are summed positively.
- Scores for the opponent's pieces are summed negatively.

### Terminal States:

- If a player has no pieces left, the evaluation returns `float('-inf')` or `float('inf')`, indicating a win or loss.

## Setup

### Clone the Repository:

```bash
git clone https://github.com/yourusername/raichu_game_ai.git
cd raichu_game_ai
```

### Ensure UTF-8 Encoding:

- Ensure all files are saved with UTF-8 encoding to avoid encoding issues.

### Run the Game:

- Navigate to the project directory and run the game using Python:

```bash
python main.py 8 w '........W.W.W.W..w.w.w.w................b.b.b.b..B.B.B.B........' 10
```

## Usage

To run the AI and see the best move for a given game state, execute the `main.py` script with the following arguments:

- **N**: The size of the board (e.g., 8 for an 8x8 board).
- **player**: The current player ('w' for white, 'b' for black).
- **board**: The current state of the board as a string.
- **timelimit**: The time limit for the AI to decide the next move in seconds.

### Example:

```bash
python main.py 8 w '........W.W.W.W..w.w.w.w................b.b.b.b..B.B.B.B........' 10
```
