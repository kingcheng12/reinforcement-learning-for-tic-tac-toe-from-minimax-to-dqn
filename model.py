"""
Reinforcement Learning for Tic-Tac-Toe: From Minimax to DQN

Assembled from your step-by-step solutions.
"""

import numpy as np

# Step 1 - create_empty_board
import numpy as np

def create_empty_board():
    """Return an empty 3x3 Tic-Tac-Toe board as an int numpy array of zeros."""
    # TODO: return a (3, 3) integer numpy array filled with zeros
    return np.zeros((3,3), dtype=int)

# Step 2 - encode_player
def encode_player(player):
    """Return the integer encoding for 'X', 'O', or 'empty'."""
    # TODO: map 'X' to 1, 'O' to -1, 'empty' to 0

    states = {'X': 1, 'O': -1, 'empty': 0}
    return states[player]

# Step 3 - print_board
import numpy as np

def print_board(board):
    """Print the 3x3 board using X, O, and . characters."""
    # TODO: render each cell as 'X' (1), 'O' (-1), or '.' (0) in a 3x3 grid
    
    symbols = {
        1: "X",
        -1: "O",
        0: ".",
    }

    for row in board:
        print(" ".join(symbols[int(cell)] for cell in row))

# Step 4 - is_cell_empty
import numpy as np

def is_cell_empty(board, row, col):
    """Return True if board[row, col] is empty (0), else False."""
    # TODO: check whether the cell at (row, col) is empty

    return board[row, col] == 0

# Step 5 - place_move
import numpy as np

def place_move(board, row, col, player):
    """Place player's mark at (row, col) and return the new board."""
    # TODO: verify the cell is empty, then return a new board with the mark placed.
    
    if not is_cell_empty(board, row, col):
        raise ValueError('cell is not empty')

    new_board = board.copy()
    new_board[row, col] = player

    return new_board

# Step 6 - get_legal_moves
import numpy as np

def get_legal_moves(board):
    """Return a list of (row, col) tuples for all empty cells on the board."""
    # TODO: scan the 3x3 board in row-major order and collect coords of empties

    legal = []
    for r in range(3):
        for c in range(3):
            if is_cell_empty(board, r, c):
                legal.append((r,c))
    return legal

# Step 7 - check_row_win
import numpy as np

def check_row_win(board, player):
    """Return True if `player` has three-in-a-row across any row of `board`."""
    # TODO: detect whether the given player has three identical marks across any row

    for row in board:
        if all([cell==player for cell in row]):
            return True

    return False

# Step 8 - check_column_win
import numpy as np

def check_column_win(board, player):
    """Return True if `player` has three-in-a-row in any column of `board`."""
    # TODO: detect whether the given player has three-in-a-row across any column

    for c in range(3):
        if all([row[c]==player for row in board]):
            return True

    return False

# Step 9 - check_main_diagonal_win
import numpy as np

def check_main_diagonal_win(board, player):
    """Return True if `player` occupies all three main-diagonal cells."""
    # TODO: check whether the main diagonal of `board` is fully occupied by `player`...

    if all([board[d][d]==player for d in range(3)]):
        return True

    return False

# Step 10 - check_anti_diagonal_win
import numpy as np

def check_anti_diagonal_win(board, player):
    # TODO: return True if `player` occupies all three anti-diagonal cells of the 3x3 board.
    if all([board[d][2-d]==player for d in range(3)]):
        return True

    return False

# Step 11 - is_winner
import numpy as np

def is_winner(board, player):
    """Return True if `player` has three-in-a-row on `board`."""
    # TODO: combine row, column, and diagonal win checks into a single boolean

    if check_row_win(board, player):
        return True
    if check_column_win(board, player):
        return True
    if check_main_diagonal_win(board, player):
        return True
    if check_anti_diagonal_win(board, player):
        return True
    
    return False

# Step 12 - is_draw
import numpy as np

def is_draw(board):
    """Return True iff the board is full and neither player has won."""
    # TODO: combine a full-board check with a no-winner check

    legal = get_legal_moves(board)

    if len(legal) <= 0 and not is_winner(board, 1) and not is_winner(board, -1):
        return True
    
    return False

# Step 13 - get_game_status
import numpy as np

def get_game_status(board):
    """Return 'X_win', 'O_win', 'draw', or 'ongoing' for the given 3x3 board."""
    # TODO: classify the board into one of the four status strings

    if is_draw(board):
        return 'draw'
    else:
        if is_winner(board, 1):
            return 'X_win'
        elif is_winner(board, -1):
            return 'O_win'
        else:
            return 'ongoing'

# Step 14 - get_current_player
import numpy as np

def get_current_player(board):
    """Return 1 if X is to move, -1 if O is to move."""
    # TODO: infer whose turn it is from the counts of X and O marks on the board
    
    X_count = 0
    O_count = 0
    for r in range(3):
        for c in range(3):
            X_count += board[r][c] == 1
            O_count += board[r][c] == -1
    
    return 1 if X_count == O_count else -1

# Step 15 - switch_player
def switch_player(player):
    """Return the opponent of `player` (1 <-> -1)."""
    # TODO: return the opposite player given 1 for X and -1 for O.

    return -player

# Step 16 - play_hardcoded_game
import numpy as np

def play_hardcoded_game(moves):
    """Replay a fixed sequence of (row, col) moves and return (final_board, status)."""
    # TODO: start from an empty board with X to move, apply moves until terminal
    board = create_empty_board()

    player = 1
    status = 'ongoing'
    for r, c in moves:
        board = place_move(board, r, c, player)
        status = get_game_status(board)
        if status != 'ongoing':
            break
        else:
            player = switch_player(player)
    
    return board, status

# Step 17 - play_interactive_game
def play_interactive_game():
    """Play a full game with two humans entering moves via stdin and return the final status."""
    # TODO: loop printing the board, reading 'row col' from stdin, applying moves until terminal
    
    board = create_empty_board()
    player = 1

    while True:
        print_board(board)

        row, col = map(int, input().split())

        try:
            board = place_move(board, row, col, player)
        except ValueError:
            continue

        status = get_game_status(board)

        if status in ("X_win", "O_win", "draw"):
            print_board(board)
            return status

        player = -player

# Step 18 - TicTacToeGame
class TicTacToeGame:
    """Stateful Tic-Tac-Toe environment wrapping the Part 1 engine."""

    def __init__(self):
        # TODO: initialize board, current_player, and status fields.
        self.board = create_empty_board()
        self.current_player = 1
        self.status = 'ongoing'

    def reset(self):
        # TODO: return board to empty starting state.
        self.board = create_empty_board()
        self.current_player = 1
        self.status = 'ongoing'

    def legal_moves(self):
        # TODO: list of (row, col) tuples still playable.
        return get_legal_moves(self.board)

    def is_terminal(self):
        # TODO: True once status is no longer 'ongoing'.
        return self.status != 'ongoing'

    def step(self, row, col):
        # TODO: play current player's move, refresh status, switch player if still ongoing.
        if self.is_terminal():
            raise ValueError("Game is already over")

        self.board = place_move(self.board, row, col, self.current_player)
        self.status = get_game_status(self.board)
        if not self.is_terminal():
            self.current_player = switch_player(self.current_player)

# Step 19 - random_move_agent
import numpy as np

def random_move_agent(board, player, rng):
    """Return a uniformly random legal (row, col) move for `player`."""
    # TODO: sample a uniformly random legal move using rng and return it as (row, col)

    legal_moves = get_legal_moves(board)
    index = rng.integers(len(legal_moves))
    return legal_moves[index]

# Step 20 - play_random_vs_random_game
def play_random_vs_random_game(rng):
    """Simulate one full random-vs-random game and return the final status."""
    # TODO: loop until terminal, alternating random moves between X and O

    game = TicTacToeGame()

    while not game.is_terminal():
        row, col = random_move_agent(game.board, game.current_player, rng)
        game.step(row, col)

    return game.status

# Step 21 - play_random_vs_random_matches
def play_random_vs_random_matches(n_games, rng):
    """Run n_games random-vs-random games and return the list of outcome strings."""
    # TODO: run n_games independent random-vs-random games and collect outcomes.

    return [play_random_vs_random_game(rng) for i in range(n_games)]

# Step 22 - compute_outcome_rates
from collections import Counter
def compute_outcome_rates(outcomes):
    """Return {'x_win_rate','o_win_rate','draw_rate'} from a list of outcome labels."""
    # TODO: count occurrences of each outcome and divide by total games
    n_games = len(outcomes)

    res_count = Counter(outcomes)

    results = {}
    results['x_win_rate'] = res_count['X_win']/n_games if n_games > 0 else 0.0
    results['o_win_rate'] = res_count['O_win']/n_games if n_games > 0 else 0.0
    results['draw_rate'] = res_count['draw']/n_games if n_games > 0 else 0.0

    return results

# Step 23 - minimax_terminal_score
def minimax_terminal_score(status):
    """Return +1 for 'X_win', -1 for 'O_win', 0 for 'draw'."""
    # TODO: map a terminal status string to its minimax leaf value.
    stutus_to_value = {'X_win': 1, 'O_win': -1, 'draw': 0}

    return stutus_to_value[status]

# Step 24 - minimax_value
def minimax_value(board, player):
    """Return the minimax value of `board` with `player` to move."""
    # TODO: terminal -> minimax_terminal_score; else max (X) / min (O) over recursive child values

    status = get_game_status(board)

    if status != "ongoing":
        return minimax_terminal_score(status)

    child_values = []

    for row, col in get_legal_moves(board):
        child_board = place_move(board, row, col, player)
        child_value = minimax_value(
            child_board,
            switch_player(player),
        )
        child_values.append(child_value)

    if player == 1:
        return max(child_values)

    if player == -1:
        return min(child_values)

# Step 25 - minimax_recursive
_minimax_cache = {}

def minimax_recursive(board, player):
    """Return the minimax value of `board` with `player` to move."""
    # TODO: recurse over legal moves, max for X (+1), min for O (-1), terminal via minimax_terminal_score
    key = (board.tobytes(), player)

    if key in _minimax_cache:
        return _minimax_cache[key]

    status = get_game_status(board)

    if status != "ongoing":
        value = minimax_terminal_score(status)
        _minimax_cache[key] = value
        return value

    child_values = []

    for row, col in get_legal_moves(board):
        child_board = place_move(board, row, col, player)

        child_value = minimax_recursive(
            child_board,
            switch_player(player),
        )
        child_values.append(child_value)

    if player == 1:
        value = max(child_values)
    elif player == -1:
        value = min(child_values)

    _minimax_cache[key] = value
    return value

# Step 26 - minimax_max_min_step
import numpy as np

def minimax_max_min_step(board, player):
    """Return (best_score, best_move) after expanding one minimax level."""
    # TODO: iterate legal moves, recurse, pick max if player == 1 else min...

    # get legal positions
    legal_moves = get_legal_moves(board)

    if len(legal_moves) == 0:
        status = get_game_status(board)
        return minimax_terminal_score(status), None
    
    if player == 1:
        best_score = float("-inf")
    elif player == -1:
        best_score = float("inf")
    else:
        raise ValueError("player must be 1 or -1")
    
    best_move = None
    next_player = switch_player(player)

    for row, col in legal_moves:
        child_board = place_move(board, row, col, player)
        score = minimax_recursive(child_board, next_player)

        if player == 1 and score > best_score:
            best_score = score
            best_move = (row, col)

        elif player == -1 and score < best_score:
            best_score = score
            best_move = (row, col)
            
    return best_score, best_move

# Step 27 - minimax_best_move
def minimax_best_move(board, player):
    """Return the optimal (row, col) move for `player` via minimax."""
    # TODO: use the minimax max/min step to pick the best legal move for player

    _, move = minimax_max_min_step(board, player)

    return move

# Step 28 - minimax_alpha_beta
import numpy as np

def minimax_alpha_beta(board, player, alpha, beta):
    """Return (best_score, best_move) for `player` using alpha-beta pruning."""
    # TODO: search the game tree with alpha-beta pruning and return (score, move)

    status = get_game_status(board)

    if status != "ongoing":
        return minimax_terminal_score(status), None
    
    legal = get_legal_moves(board)
    best_move = None

    if player == 1:
        value = float("-inf")

        for row, col in legal:
            child_board = place_move(board, row, col, player)

            child_value, child_move = minimax_alpha_beta(
                child_board,
                switch_player(player),
                alpha,
                beta,
            )
            if child_value > value:
                best_move = (row, col)

            value = max(value, child_value)
            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value, best_move

    if player == -1:
        value = float("inf")

        for row, col in legal:
            child = place_move(board, row, col, player)
            child_value, child_move = minimax_alpha_beta(
                child,
                switch_player(player),
                alpha,
                beta,
            )
            if child_value < value:
                best_move = (row, col)
            value = min(value, child_value)
            beta = min(beta, value)

            if alpha >= beta:
                break

        return value, best_move

# Step 29 - play_minimax_vs_random_matches
def play_minimax_vs_random_matches(n_games, minimax_plays_x, rng):
    # TODO: run n_games of minimax vs random and return aggregated outcome rates.
    statuses = []

    minimax_player = 1 if minimax_plays_x else -1

    for _ in range(n_games):
        game = TicTacToeGame()

        while not game.is_terminal():
            player = game.current_player

            if player == minimax_player:
                _, move = minimax_max_min_step(
                    game.board,
                    player,
                )
            else:
                move = random_move_agent(
                    game.board,
                    player,
                    rng,
                )

            row, col = move
            game.step(row, col)

        statuses.append(game.status)

    return compute_outcome_rates(statuses)

# Step 30 - play_minimax_vs_minimax_matches
def play_minimax_vs_minimax_matches(n_games):
    """Play n_games minimax-vs-minimax games and report outcome rates plus an all_draws flag."""
    # TODO: simulate n_games minimax-vs-minimax games and aggregate outcome rates.
    statuses = []

    player = 1

    for _ in range(n_games):
        game = TicTacToeGame()

        while not game.is_terminal():
            player = game.current_player
            _, move = minimax_max_min_step(
                game.board,
                player,
            )

            row, col = move
            game.step(row, col)

        statuses.append(game.status)

    results = compute_outcome_rates(statuses)
    results['all_draws'] = results['draw_rate'] == 1 or n_games <= 0

    return results

# Step 31 - encode_board_state_key
import numpy as np

def encode_board_state_key(board):
    """Encode a 3x3 board as a length-9 string over {'0','1','2'} in row-major order."""
    # TODO: map each cell (0, 1, -1) to a single character and join row-major.
    
    encoded = ''
    mapping = {'0': '0', '1': '1', '-1':'2'}
    for row in range(3):
        for col in range(3):
            encoded += mapping[str(board[row][col])]
    
    return encoded

# Step 32 - canonical_board_key
def canonical_board_key(board):
    # TODO: return the lex-smallest encoded key over all 8 symmetries of the board.

    keys = []

    for _ in range(4):
        board = np.rot90(board)
        keys.append(encode_board_state_key(board))
        filp_board = np.flip(board)
        keys.append(encode_board_state_key(filp_board))
    
    return min(keys)

# Step 33 - initialize_q_table
from collections import defaultdict

def initialize_q_table():
    """Create an empty Q-table that returns 0.0 for unseen (state, action) keys."""
    # TODO: return a mapping where missing (state_key, action) lookups yield 0.0

    q_table = defaultdict(float)

    return q_table

# Step 34 - get_q_value
def get_q_value(q_table, state_key, action):
    # TODO: return Q(state_key, action), or 0.0 if the pair is not in the table
    
    return q_table.get((state_key, action), 0)

# Step 35 - set_q_value
def set_q_value(q_table, state_key, action, value):
    """Write a new Q-value for a (state, action) pair into the Q-table."""
    # TODO: store value under the (state_key, action) key in q_table.
    q_table[(state_key, action)] = value

# Step 36 - choose_learning_rate_alpha
def choose_learning_rate_alpha():
    """Return the learning rate alpha (float in (0, 1]) for tabular Q-learning."""
    # TODO: return a float in (0, 1] to use as the Q-learning step size.

    return 0.1

# Step 37 - choose_discount_factor_gamma
def choose_discount_factor_gamma():
    """Return the discount factor gamma in [0, 1] for Q-learning."""
    # TODO: return a float discount factor in [0, 1] for tabular Q-learning.
    return 0.9

# Step 38 - choose_initial_epsilon
def choose_initial_epsilon():
    """Return the starting exploration rate epsilon for epsilon-greedy."""
    # TODO: return the starting exploration rate in [0, 1] favoring exploration
    return 1.0

# Step 39 - epsilon_decay_schedule
import numpy as np

def epsilon_decay_schedule(initial_epsilon, episode_index, min_epsilon, decay_rate):
    """Return the decayed epsilon for the given episode, clipped to min_epsilon."""
    # TODO: compute exponential decay of initial_epsilon over episode_index, clipped to a floor.

    epsilon = initial_epsilon * np.exp(-decay_rate*episode_index)

    return max(min_epsilon, epsilon)

# Step 40 - epsilon_greedy_explore_move
def epsilon_greedy_explore_move(legal_actions, rng):
    """Sample a uniformly random legal action from legal_actions using rng."""
    # TODO: pick one action uniformly at random from legal_actions using rng

    index = rng.integers(len(legal_actions))
    return legal_actions[index]

# Step 41 - epsilon_greedy_select_action
def epsilon_greedy_select_action(q_table, state_key, legal_actions, epsilon, rng):
    """Choose an action via epsilon-greedy over the legal actions."""
    # TODO: with probability epsilon explore, else pick the greedy legal action.
    
    p = rng.binomial(n=1, p=epsilon)

    if p == 1:
        move = epsilon_greedy_explore_move(legal_actions, rng)
    else:
        move = greedy_argmax_over_legal_actions(q_table, state_key, legal_actions, rng)
    
    return move

# Step 42 - greedy_argmax_over_legal_actions
def greedy_argmax_over_legal_actions(q_table, state_key, legal_actions, rng):
    """Return the legal action with the highest Q-value (random tie-break)."""
    # TODO: return the legal action with the highest Q(state_key, action)...
    q_values = [
        q_table.get((state_key, action), 0.0)
        for action in legal_actions
    ]

    max_q = max(q_values)

    best_actions = [
        action
        for action, q_value in zip(legal_actions, q_values)
        if q_value == max_q
    ]

    index = rng.integers(len(best_actions))
    return best_actions[index]

# Step 43 - random_tie_break_argmax
def random_tie_break_argmax(values, candidates, rng):
    """Return one candidate whose value equals max(values), tie-broken uniformly at random."""
    # TODO: pick a candidate whose value equals the maximum, breaking ties uniformly with rng.
    
    max_value = max(values)

    best_cand = [cand for cand, value in zip(candidates, values) if value == max_value]

    index = rng.choice(len(best_cand))

    return best_cand[index]

# Step 44 - tic_tac_toe_reward
def tic_tac_toe_reward(game_status, agent_player):
    """Return scalar reward from the agent's perspective.

    game_status: one of 'X_win', 'O_win', 'draw', 'ongoing'.
    agent_player: +1 for X, -1 for O.
    """
    # TODO: map terminal status to +/-1 from the agent's perspective, 0 otherwise
    
    if game_status == 'draw' or game_status == 'ongoing':
        return 0
    
    if game_status == 'X_win':
        return agent_player
    
    if game_status == 'O_win':
        return -agent_player

# Step 45 - q_learning_nonterminal_target
def q_learning_nonterminal_target(reward, gamma, q_table, next_state_key, next_legal_actions):
    """Return the TD target r + gamma * max_a' Q(s', a') over legal next actions."""
    # TODO: compute the bootstrapped Q-learning target for a non-terminal transition
    
    if len(next_legal_actions) == 0:
        best_q = 0
    else:
        best_q = max([q_table[(next_state_key, action)] for action in next_legal_actions])

    td = reward + gamma * best_q

    return td

# Step 46 - q_learning_terminal_target
def q_learning_terminal_target(reward):
    """Return the TD target for a terminal transition."""
    # TODO: return the terminal TD target given the observed reward.

    return reward

# Step 47 - q_learning_update
def q_learning_update(q_table, state_key, action, target, alpha):
    """Apply Q(s,a) <- Q(s,a) + alpha * (target - Q(s,a)) and return the new value."""
    # TODO: read current Q via get_q_value, move toward target by alpha, write back with set_q_value

    current_q = get_q_value(q_table, state_key, action)
    updated_q = current_q + alpha * (target - current_q)
    set_q_value(q_table, state_key, action, updated_q)

    return updated_q

# Step 48 - episode_reset_game
import numpy as np

def episode_reset_game():
    """Return a fresh empty board and the starting player (+1 for X)."""
    # TODO: build a new empty board and return it alongside the starting player

    board = create_empty_board()

    return board, 1

# Step 49 - episode_agent_pick_action
def episode_agent_pick_action(q_table, board, current_player, epsilon, rng):
    # TODO: return (canonical_state_key, action_index_0_to_8) using epsilon-greedy over legal moves.

    state_key = canonical_board_key(board)

    legal_moves = get_legal_moves(board)
    legal_actions = [
        row * 3 + col
        for row, col in legal_moves
    ]

    action_index = epsilon_greedy_select_action(
        q_table,
        state_key,
        legal_actions,
        epsilon,
        rng,
    )

    return state_key, action_index

# Step 50 - episode_apply_action
def episode_apply_action(board, action, current_player, agent_player):
    """Apply one move, return next_board/next_player/status/reward/done."""
    # TODO: convert action to (row, col), place the move, then evaluate status and reward.
    
    row, col = action // 3, action % 3
    board = place_move(board, row, col, current_player)

    status = get_game_status(board)
    done = status != "ongoing"

    if done:
        reward = minimax_terminal_score(status) * agent_player
    else:
        reward = 0

    next_player = switch_player(current_player)

    return {'next_board': board,
            'next_player': next_player,
            'status': status,
            'reward': reward,
            "done": done,
            }

# Step 51 - episode_apply_q_update
def episode_apply_q_update(q_table, state_key, action, reward, next_board, done, alpha, gamma):
    """Compute the TD target (terminal or nonterminal) and apply the Q-learning update."""
    # TODO: branch on done, build the appropriate target, then call the update helper.
    current_q = get_q_value(q_table, state_key, action)

    if done:
        td_target = reward
    else:
        next_state_key = canonical_board_key(next_board)
        legal_actions = get_legal_moves(next_board)

        if legal_actions:
            max_next_q = max(
                get_q_value(q_table, next_state_key, next_action)
                for next_action in legal_actions
            )
        else:
            max_next_q = 0.0

        td_target = reward + gamma * max_next_q

    new_q = current_q + alpha * (td_target - current_q)
    set_q_value(q_table, state_key, action, new_q)

    return new_q

# Step 52 - episode_check_terminate
def episode_check_terminate(status):
    """Return True if status is terminal (win or draw), else False."""
    # TODO: return True when status indicates the episode should end

    return status != 'ongoing'

# Step 53 - train_q_learning_agent
def train_q_learning_agent(num_episodes, alpha, gamma, initial_epsilon, min_epsilon, decay_rate, opponent_policy, rng):
    # TODO: run N Q-learning episodes vs opponent_policy, decay epsilon, return q_table and outcomes
    
    q_table = initialize_q_table()
    episode_outcomes = []
    agent_player = 1

    for episode in range(num_episodes):
        epsilon = epsilon_decay_schedule(initial_epsilon, episode, min_epsilon, decay_rate)
        board, current_player = episode_reset_game()

        while True:
            state_key, action_index = episode_agent_pick_action(q_table, board, current_player, epsilon, rng)
            stats = episode_apply_action(board, action_index, current_player, agent_player)
            
            if not stats['done']:
                opponent_move = opponent_policy(stats['next_board'], stats['next_player'], rng)
                stats = episode_apply_action(stats['next_board'], opponent_move, stats['next_player'], agent_player)

            # stats['next_board'] represent the board when the next time agent take action
            # we find the best results to update current board
            new_q = episode_apply_q_update(q_table, state_key, action_index, stats['reward'], stats['next_board'], stats['done'], alpha, gamma)

            board = stats["next_board"]
            current_player = stats["next_player"]

            if stats['done']:
                episode_outcomes.append(stats['status'])
                break
    
    return {'q_table': q_table, 'episode_outcomes': episode_outcomes}

# Step 54 - compute_batched_outcome_stats
import numpy as np

def compute_batched_outcome_stats(episode_outcomes, batch_size):
    """Aggregate outcomes into per-batch win/loss/draw rates."""
    # TODO: group outcomes into chunks of batch_size and compute rates per chunk
    num_batches = len(episode_outcomes) // batch_size

    batch_indices = np.arange(num_batches)
    win_rates = np.empty(num_batches, dtype=float)
    loss_rates = np.empty(num_batches, dtype=float)
    draw_rates = np.empty(num_batches, dtype=float)

    for batch_index in range(num_batches):
        start = batch_index * batch_size
        end = start + batch_size
        batch = episode_outcomes[start:end]

        win_rates[batch_index] = batch.count("win") / batch_size
        loss_rates[batch_index] = batch.count("loss") / batch_size
        draw_rates[batch_index] = batch.count("draw") / batch_size

    return {
        "batch_index": batch_indices,
        "win_rate": win_rates,
        "loss_rate": loss_rates,
        "draw_rate": draw_rates,
    }

# Step 55 - self_play_episode
def self_play_episode(q_table, alpha, gamma, epsilon, rng):
    """Run one self-play episode and return final_status and a list of transitions."""
    # TODO: loop until terminal, picking actions with episode_agent_pick_action and applying them

    # create board
    # define player
    board, current_player = episode_reset_game()
    transitions = []

    # loop
    ## one player plays
    ## update q_table
    ## check terminal
    while True:
        state_key, action_index = episode_agent_pick_action(q_table, board, current_player, epsilon, rng)
        transition = episode_apply_action(board, action_index, current_player, current_player)
        transitions.append({
            "state_key": state_key,
            "action": action_index,
            "reward": transition["reward"],
            "next_board": transition["next_board"],
            "done": transition["done"],
            "player": current_player,
        })

        board = transition["next_board"]
        current_player = transition["next_player"]

        if transition['done']:
            break
    
    return {'final_status': transition['status'],
            'transitions': transitions
            }

# Step 56 - flip_board_perspective
import numpy as np

def flip_board_perspective(board, current_player):
    """Return a board view where current_player's marks are +1."""
    # TODO: return a new (3,3) int array expressed from current_player's perspective

    return board * current_player

# Step 57 - perspective_reward_sign
def perspective_reward_sign(reward, acting_player, scoring_player):
    """Return reward expressed from acting_player's perspective."""
    # TODO: flip the sign of reward when acting_player and scoring_player differ

    sign = -1 if acting_player != scoring_player else 1

    return sign * reward

# Step 58 - train_q_agent_self_play
def train_q_agent_self_play(num_episodes, alpha, gamma, initial_epsilon, min_epsilon, decay_rate, rng):
    # TODO: run num_episodes of self-play, applying Q-learning updates with perspective flipping.
    q_table = initialize_q_table()
    episode_outcomes = []

    for episode in range(num_episodes):
        epsilon = epsilon_decay_schedule(initial_epsilon, episode, min_epsilon, decay_rate)

        result = self_play_episode(q_table, alpha, gamma, epsilon, rng) # only record moves but not update q_table
        final_status = result["final_status"]
        episode_outcomes.append(final_status)
        transitions = result["transitions"]

        # update q_table
        for transition in reversed(transitions):
            state_key = transition["state_key"]
            action = transition["action"]
            player = transition["player"]
            next_board = transition["next_board"]
            done = transition["done"]

            current_q = get_q_value(
                q_table,
                state_key,
                action,
            )
            if done:
                if final_status == 'draw':
                    reward = 0
                else:
                    scoring_player = 1 if final_status == "X_win" else -1
                    score = minimax_terminal_score(final_status)
                    reward = perspective_reward_sign(score, player, scoring_player)
                td_target = reward
            else:
                next_player = switch_player(player)
                perspective_next_board = flip_board_perspective(
                    next_board,
                    next_player,
                )
                next_state_key = canonical_board_key(
                    perspective_next_board
                )

                legal_moves = get_legal_moves(next_board)
                legal_actions = [
                    row * 3 + col
                    for row, col in legal_moves
                ]

                if legal_actions:
                    max_next_q = max(
                        get_q_value(
                            q_table,
                            next_state_key,
                            next_action,
                        )
                        for next_action in legal_actions
                    )
                else:
                    max_next_q = 0.0

                # reward = 0
                td_target = -gamma * max_next_q

            new_q = current_q + alpha * (td_target - current_q)

            set_q_value(
                q_table,
                state_key,
                action,
                new_q,
            )

    return {
        "q_table": q_table,
        "episode_outcomes": episode_outcomes,
    }

# Step 59 - evaluate_q_agent_vs_random
def evaluate_q_agent_vs_random(q_table, num_games, rng):
    """Play num_games between the greedy Q-agent and a random opponent.

    Returns a dict with keys 'wins', 'losses', 'draws' (ints) and
    'win_rate', 'loss_rate', 'draw_rate' (floats), all from the agent's
    perspective. The agent alternates between playing X and O across games.
    """
    # TODO: simulate num_games and tally outcomes from the agent's perspective
    wins = 0
    losses = 0
    draws = 0

    game = TicTacToeGame()

    for game_index in range(num_games):
        game.reset()
        agent_player = 1 if game_index % 2 == 0 else -1
        while not game.is_terminal():
            current_player = game.current_player
            if current_player == agent_player:
                # q_table is trained with agent player as X
                perspective_board = flip_board_perspective(
                    game.board,
                    current_player,
                )
                state_key = canonical_board_key(perspective_board)

                legal_actions = [
                    row * 3 + col
                    for row, col in get_legal_moves(game.board)
                ]
                action = greedy_argmax_over_legal_actions(
                    q_table,
                    state_key,
                    legal_actions,
                    rng,
                )
            else:
                legal_actions = get_legal_moves(game.board)
                row, col = random_move_agent(
                    game.board,
                    current_player,
                    rng,
                )
                action = row * 3 + col

            row, col = action//3, action%3        
            game.step(row, col)

        if game.status == "draw":
            draws += 1
        elif (
            game.status == "X_win" and agent_player == 1
        ) or (
            game.status == "O_win" and agent_player == -1
        ):
            wins += 1
        else:
            losses += 1

    if num_games == 0:
        win_rate = 0.0
        loss_rate = 0.0
        draw_rate = 0.0
    else:
        win_rate = wins / num_games
        loss_rate = losses / num_games
        draw_rate = draws / num_games

    return {
        "wins": wins,
        "losses": losses,
        "draws": draws,
        "win_rate": win_rate,
        "loss_rate": loss_rate,
        "draw_rate": draw_rate,
    }

# Step 60 - evaluate_q_agent_vs_minimax
def evaluate_q_agent_vs_minimax(q_table, num_games, rng):
    # TODO: play num_games matches alternating X/O between Q-agent and minimax, return agent-perspective rates.
    wins = 0
    losses = 0
    draws = 0

    game = TicTacToeGame()

    for game_index in range(num_games):
        game.reset()
        agent_player = 1 if game_index % 2 == 0 else -1
        while not game.is_terminal():
            current_player = game.current_player
            if current_player == agent_player:
                # q_table is trained with agent player as X
                perspective_board = flip_board_perspective(
                    game.board,
                    current_player,
                )
                state_key = canonical_board_key(perspective_board)

                legal_actions = [
                    row * 3 + col
                    for row, col in get_legal_moves(game.board)
                ]
                action = greedy_argmax_over_legal_actions(
                    q_table,
                    state_key,
                    legal_actions,
                    rng,
                )
            else:
                _, move = minimax_alpha_beta(
                    game.board,
                    current_player,
                    float("-inf"),
                    float("inf"),
                )
                row, col = move
                action = row * 3 + col

            row, col = action//3, action%3
            game.step(row, col)

        if game.status == "draw":
            draws += 1
        elif (
            game.status == "X_win" and agent_player == 1
        ) or (
            game.status == "O_win" and agent_player == -1
        ):
            wins += 1
        else:
            losses += 1

    if num_games == 0:
        win_rate = 0.0
        loss_rate = 0.0
        draw_rate = 0.0
    else:
        win_rate = wins / num_games
        loss_rate = losses / num_games
        draw_rate = draws / num_games

    return {
        "x_win_rate": win_rate,
        "o_win_rate": loss_rate,
        "draw_rate": draw_rate,
    }

# Step 61 - inspect_q_values_for_state
import numpy as np

def inspect_q_values_for_state(q_table, board, current_player):
    """Print the board and Q-values for all 9 cells; return a length-9 array."""
    # TODO: look up Q-values for every cell of the board and pretty-print them.

    state_key = canonical_board_key(board)

    print_board(board)
    q_values = []

    for row in range(3):
        row_values = []
        for col in range(3):
            action = (row, col)
            q_value = get_q_value(
                q_table,
                state_key,
                action,
            )
            q_values.append(q_value)
            row_values.append(q_value)

        print(" ".join(f"{value:+.2f}" for value in row_values))

    return np.asarray(q_values, dtype = float)

# Step 62 - serialize_q_table_to_dict
def serialize_q_table_to_dict(q_table):
    """Convert a Q-table (str -> np.ndarray shape (9,)) into a plain dict (str -> list of floats)."""
    # TODO: convert each numpy array value into a plain Python list of floats
    out = {}
    for key, val in q_table.items():
        out[key] = np.astype(val, float).tolist()

    return out

# Step 63 - deserialize_q_table_from_dict
import numpy as np

def deserialize_q_table_from_dict(serialized):
    """Rebuild a Q-table (state_key -> np.ndarray shape (9,)) from a plain dict."""
    # TODO: convert each list value back into a numpy float array of shape (9,)
    
    q_table = {}

    for key, val in serialized.items():
        q_table[key] = np.asarray(val)

    return q_table

# Step 64 - encode_board_flat_length_nine
import numpy as np

def encode_board_flat_length_nine(board, current_player):
    """Encode a 3x3 board as a length-9 float32 vector from current_player's view."""
    # TODO: relabel pieces so own=+1, opponent=-1, empty=0, then flatten to (9,) float32
    
    perspective_board = flip_board_perspective(board, current_player)

    return perspective_board.flatten().astype(np.float32)

# Step 65 - encode_board_one_hot_length_eighteen
import numpy as np

def encode_board_one_hot_length_eighteen(board, current_player):
    """Encode a 3x3 board as a length-18 two-channel one-hot vector."""
    # TODO: build own-piece and opponent-piece masks, flatten and concatenate
    
    own = (board == current_player).astype(np.float32)
    opponent = (
        board == switch_player(current_player)
    ).astype(np.float32)

    return np.concatenate([
        own.reshape(-1),
        opponent.reshape(-1),])

# Step 66 - build_mlp_architecture
def build_mlp_architecture(input_dim, hidden_dim, output_dim=9):
    # TODO: return a dict describing input_dim -> hidden_dim -> output_dim layer sizes.
    
    return {'input_dim': input_dim, 'hidden_dim': hidden_dim, 'output_dim': output_dim}

# Step 67 - initialize_mlp_parameters
def initialize_mlp_parameters(architecture, seed=0):
    """Initialize MLP weights with He init and zero biases.

    architecture: dict from build_mlp_architecture with input_dim, hidden_dim, output_dim.
    seed: int seed for numpy RNG.
    Returns dict with keys 'W1', 'b1', 'W2', 'b2'.
    """
    # TODO: sample weights with He init and zero the biases
    input_dim = architecture["input_dim"]
    hidden_dim = architecture["hidden_dim"]
    output_dim = architecture["output_dim"]

    rng = np.random.RandomState(seed)

    W1 = (
        rng.randn(input_dim, hidden_dim)
        * np.sqrt(2.0 / input_dim)
    ).astype(np.float32)

    b1 = np.zeros(hidden_dim, dtype=np.float32)

    W2 = (
        rng.randn(hidden_dim, output_dim)
        * np.sqrt(2.0 / hidden_dim)
    ).astype(np.float32)

    b2 = np.zeros(output_dim, dtype=np.float32)

    return {
        "W1": W1,
        "b1": b1,
        "W2": W2,
        "b2": b2,
    }

# Step 68 - mlp_forward_pass
def mlp_forward_pass(params, x):
    """Forward pass through a two-layer MLP with ReLU hidden activation.

    Args:
        params: dict with keys 'W1', 'b1', 'W2', 'b2'.
        x: np.ndarray of shape (batch, input_dim).

    Returns:
        (q_values, cache) where q_values has shape (batch, output_dim) and
        cache is a dict with keys {'x', 'z1', 'h1', 'q'}.
    """
    # TODO: compute z1 = x W1 + b1, h1 = ReLU(z1), q = h1 W2 + b2, cache intermediates.
    W1 = params['W1']
    b1 = params['b1']
    W2 = params['W2']
    b2 = params['b2']

    z1 = x @ W1 + b1

    h1 = np.where(z1 > 0, z1, 0)

    q = h1 @ W2 + b2

    cache = {}
    cache['x'] = x
    cache['z1'] = z1
    cache['h1'] = h1
    cache['q'] = q

    return q, cache

# Step 69 - mask_illegal_actions_neg_inf
import numpy as np

def mask_illegal_actions_neg_inf(q_values, legal_action_mask):
    """Return a copy of q_values with illegal entries set to -inf."""
    # TODO: replace q-values at positions where the mask is False with -inf

    return np.where(legal_action_mask, q_values, -np.inf)

# Step 70 - argmax_action_from_q_values
import numpy as np

def argmax_action_from_q_values(masked_q_values):
    """Return the index of the largest entry in masked_q_values as an int."""
    # TODO: pick the action index with the highest (masked) Q-value

    index = np.argmax(masked_q_values, axis = -1)

    return index

# Step 71 - mse_loss_on_chosen_action
import numpy as np

def mse_loss_on_chosen_action(predicted_q, action_indices, target_q):
    """MSE between Q(s, a_taken) and the bootstrapped target Q."""
    # TODO: gather one Q-value per row using action_indices, then mean squared error vs target_q.

    batch_indices = np.arange(predicted_q.shape[0])
    chosen_q = predicted_q[batch_indices, action_indices]

    return np.mean((chosen_q - target_q) ** 2)

# Step 72 - mlp_backward_pass
def mlp_backward_pass(params, cache, action_indices, target_q):
    """Backprop MSE-on-chosen-action loss through the MLP and return param gradients."""
    # TODO: compute gradients dW1, db1, dW2, db2 for the MSE-on-chosen-action loss

    x = cache["x"]
    z1 = cache["z1"]
    h1 = cache["h1"]
    predicted_q = cache["q"]

    action_indices = np.asarray(action_indices, dtype=int)
    target_q = np.asarray(target_q, dtype=np.float32)

    batch_size = predicted_q.shape[0]
    batch_indices = np.arange(batch_size)

    chosen_q = predicted_q[batch_indices, action_indices]

    # L = mean((chosen_q - target_q) ** 2)
    d_chosen_q = (2.0 / batch_size) * (chosen_q - target_q)

    # Only chosen actions receive gradients.
    d_predicted_q = np.zeros_like(predicted_q)
    d_predicted_q[batch_indices, action_indices] = d_chosen_q

    # Output layer: predicted_q = h1 @ W2 + b2
    dW2 = h1.T @ d_predicted_q
    db2 = np.sum(d_predicted_q, axis=0)

    # Propagate into hidden layer.
    dh1 = d_predicted_q @ params["W2"].T

    # ReLU derivative.
    dz1 = dh1 * (z1 > 0)

    # First layer: z1 = x @ W1 + b1
    dW1 = x.T @ dz1
    db1 = np.sum(dz1, axis=0)

    return {
        "W1": dW1,
        "b1": db1,
        "W2": dW2,
        "b2": db2,
    }

# Step 73 - adam_update_step
import numpy as np

def adam_update_step(params, grads, adam_state, learning_rate=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    # TODO: perform one Adam step; update adam_state's moments and step counter, return (new_params, adam_state).

    if not adam_state:
        adam_state = {
            "m": {
                name: np.zeros_like(param)
                for name, param in params.items()
            },
            "v": {
                name: np.zeros_like(param)
                for name, param in params.items()
            },
            "t": 0,
        }

    t = adam_state["t"] + 1
    new_params = {}
    new_m = {}
    new_v = {}

    for name, param in params.items():
        grad = grads[name]

        m = (
            beta1 * adam_state["m"][name]
            + (1.0 - beta1) * grad
        )
        v = (
            beta2 * adam_state["v"][name]
            + (1.0 - beta2) * grad ** 2
        )

        m_hat = m / (1.0 - beta1 ** t)
        v_hat = v / (1.0 - beta2 ** t)

        new_params[name] = (
            param
            - learning_rate
            * m_hat
            / (np.sqrt(v_hat) + eps)
        )

        new_m[name] = m
        new_v[name] = v

    new_state = {
        "m": new_m,
        "v": new_v,
        "t": t,
    }

    return new_params, new_state

# Step 74 - create_replay_buffer
from collections import deque


def create_replay_buffer(capacity):
    """Return an empty replay buffer with a fixed maximum capacity."""
    # TODO: build a dict holding an empty bounded deque and the capacity

    data = deque(maxlen = capacity)

    return {'data': data, 'capacity': capacity}

# Step 75 - append_transition_to_buffer
def append_transition_to_buffer(buffer, state, action, reward, next_state, done, next_legal_mask):
    """Append one (s, a, r, s', done, next_legal_mask) transition to the replay buffer."""
    # TODO: store the transition tuple in buffer['data']
    
    data = (state, action, reward, next_state, done, next_legal_mask)

    # note old data will be drop if reach maxlen
    buffer['data'].append(data)

    return buffer

# Step 76 - cap_buffer_size_drop_oldest
def cap_buffer_size_drop_oldest(buffer):
    """Drop oldest transitions until len(buffer['data']) <= buffer['capacity']."""
    # TODO: pop from the front of buffer['data'] until it fits the capacity.

    if isinstance(buffer['data'], deque):
        while len(buffer['data']) > buffer['capacity'] and len(buffer['data']) > 0:
            buffer['data'].popleft()
    elif isinstance(buffer['data'], list):
        while len(buffer['data']) > buffer['capacity'] and len(buffer['data']) > 0:
            buffer['data'].pop(0)

    return buffer

# Step 77 - sample_minibatch_from_buffer
import numpy as np


def sample_minibatch_from_buffer(buffer, batch_size, rng):
    """Draw `batch_size` random transitions from `buffer` and stack fields into arrays."""
    # TODO: draw a uniformly random minibatch of transitions and stack each field.
    data = buffer["data"]
    batch_indices = rng.choice(
        len(data),
        size=batch_size,
        replace=True,
    )

    selected = [buffer['data'][int(i)] for i in batch_indices]

    field_mapping = {
        "states": "state",
        "actions": "action",
        "rewards": "reward",
        "next_states": "next_state",
        "dones": "done",
        "next_legal_masks": "next_legal_mask",
    }

    return {
        output_key: np.stack([
            np.asarray(transition[input_key])
            for transition in selected
        ])
        for output_key, input_key in field_mapping.items()
    }

# Step 78 - build_target_network_copy
import numpy as np
import copy

def build_target_network_copy(online_params):
    """Return a deep copy of the online MLP parameter dict."""
    # TODO: return a new dict whose arrays are independent copies of online_params

    return {
        key: value.copy().astype(np.float64)
        for key, value in online_params.items()
    }

# Step 79 - compute_target_q_with_target_network
import numpy as np

def compute_target_q_with_target_network(target_params, batch, gamma):
    """Compute DQN bootstrap targets r + gamma * max_a' Q_target(s', a')."""
    # TODO: forward next_states through the target net, mask illegal actions, take max, zero on terminals

    # for each transition in batch
    # compute next state via frozen target network to get q
    # mask legal action to -inf
    # take max of remaining actions
    # calculate q
    rewards = np.asarray(batch["rewards"], dtype=np.float32)
    dones = np.asarray(batch["dones"], dtype=bool)
    next_states = np.asarray(batch["next_states"])
    next_legal_masks = np.asarray(
        batch["next_legal_masks"],
        dtype=bool,
    )

    next_q_values, cache = mlp_forward_pass(
        target_params,
        next_states,
    )

    masked_next_q = mask_illegal_actions_neg_inf(
        next_q_values,
        next_legal_masks,
    )
    max_next_q = np.max(masked_next_q, axis=1)

    target_q = np.where(
        dones,
        rewards,
        rewards + gamma * max_next_q,
    )

    return target_q

# Step 80 - sync_target_network_periodically
import numpy as np

def sync_target_network_periodically(online_params, target_params, step_count, sync_every_k):
    """Copy online -> target every sync_every_k steps; otherwise leave target unchanged."""
    # TODO: refresh target_params from online_params when step_count is a positive multiple of sync_every_k

    if step_count > 0 and step_count % sync_every_k == 0:
        target_params = build_target_network_copy(online_params)
    return target_params

# Step 81 - dqn_select_action
def dqn_select_action(online_params, state, legal_mask, epsilon, rng):
    """Epsilon-greedy action index over the legal moves."""
    # TODO: explore with prob epsilon (random legal action) else argmax of masked Q-values
    
    r = rng.random()

    if r <= epsilon:
        legal_actions = [i for i in range(len(legal_mask)) if legal_mask[i]]
        action = rng.choice(legal_actions)
    else:
        q_values, cache = mlp_forward_pass(
            online_params,
            state,
        )
        masked_q_values = mask_illegal_actions_neg_inf(
            q_values,
            legal_mask,
        )
        action = np.argmax(masked_q_values, axis=-1)
    
    return int(action)

# Step 82 - dqn_train_step
def dqn_train_step(online_params, target_params, adam_state, buffer, batch_size, gamma, lr, rng):
    """Run one DQN minibatch update. Return (online_params, adam_state, loss)."""
    # TODO: sample -> targets -> forward -> loss -> backward -> adam step

    batch = sample_minibatch_from_buffer(buffer, batch_size, rng)

    target = compute_target_q_with_target_network(target_params, batch, gamma)

    predicted_q, cache = mlp_forward_pass(online_params, batch['states'])

    loss = mse_loss_on_chosen_action(predicted_q, batch['actions'], target)

    grads = mlp_backward_pass(online_params, cache, batch['actions'], target)

    new_params, new_state = adam_update_step(online_params, grads, adam_state, learning_rate = lr)

    return new_params, new_state, loss

# Step 83 - train_dqn_agent
def train_dqn_agent(num_episodes, hidden_dim=64, gamma=0.99, lr=1e-3, batch_size=64, buffer_capacity=10000, sync_every_k=200, epsilon_start=1.0, epsilon_end=0.05, seed=0):
    """Full DQN self-play training loop. Returns dict with online_params,
    target_params, loss_history, reward_history, architecture."""
    # TODO: run num_episodes of self-play, store transitions, train with Adam.

    rng = np.random.default_rng(seed)
    architecture = build_mlp_architecture(input_dim=9, hidden_dim=hidden_dim, output_dim=9)
    online_params = initialize_mlp_parameters(architecture, seed)
    target_params = build_target_network_copy(online_params)
    adam_state = {}
    buffer = create_replay_buffer(buffer_capacity)

    loss_history = []
    reward_history = []
    for episode in range(num_episodes):
        if num_episodes <= 1:
            progress = 1.0
        else:
            progress = episode / (num_episodes - 1)
        epsilon = epsilon_start+ progress * (epsilon_end - epsilon_start)

        board, current_player = episode_reset_game()
        episode_reward = 0.0
        done = False

        while not done:
            # Encode from the acting player's perspective.
            state = encode_board_flat_length_nine(
                board,
                current_player,
            )
            legal_moves = get_legal_moves(board)
            legal_actions = [
                row * 3 + col
                for row, col in legal_moves
            ]
            legal_action_mask = np.zeros(9, dtype=bool)
            legal_action_mask[legal_actions] = True

            action = dqn_select_action(
                online_params,
                state,
                legal_action_mask,
                epsilon,
                rng,
            )

            row = action // 3
            col = action % 3

            next_board = place_move(
                board,
                row,
                col,
                current_player,
            )
            status = get_game_status(next_board)
            done = status != "ongoing"

            # Reward from the acting player's perspective.
            if done:
                reward = (
                    minimax_terminal_score(status)
                    * current_player
                )
            else:
                reward = 0.0
            episode_reward += reward
            next_player = switch_player(current_player)

            next_state = encode_board_flat_length_nine(
                next_board,
                next_player,
            )

            if done:
                next_legal_mask = np.zeros(9, dtype=bool)
            else:
                next_legal_mask = np.zeros(9, dtype=bool)

                for next_row, next_col in get_legal_moves(next_board):
                    next_action = next_row * 3 + next_col
                    next_legal_mask[next_action] = True

            transition = {
                "state": state,
                "action": action,
                "reward": reward,
                "next_state": next_state,
                "done": done,
                "next_legal_mask": next_legal_mask,
            }
            buffer["data"].append(transition)
            cap_buffer_size_drop_oldest(buffer)
            board = next_board
            current_player = next_player


        # Start training once one full minibatch is available.
        if len(buffer["data"]) >= batch_size:
            online_params, adam_state, loss = dqn_train_step(
                online_params=online_params,
                target_params=target_params,
                adam_state=adam_state,
                buffer=buffer,
                batch_size=batch_size,
                gamma=gamma,
                lr=lr,
                rng=rng,
            )
            loss_history.append(float(loss))

        reward_history.append(float(episode_reward))

        target_params = sync_target_network_periodically(
            online_params,
            target_params,
            episode + 1,
            sync_every_k,
        )


    return {
        "online_params": online_params,
        "target_params": target_params,
        "loss_history": loss_history,
        "reward_history": reward_history,
        "architecture": architecture,
    }

# Step 84 - compare_dqn_tabular_random_minimax
def compare_dqn_tabular_random_minimax(dqn_artifacts, q_table, num_games=200):
    """Round-robin evaluation among DQN, tabular Q, random, and minimax agents."""
    # TODO: play num_games for each of the six pairings, alternating X, and report rates
    online_params = dqn_artifacts["online_params"]
    rng = np.random.default_rng(0)

    agent_names = ["dqn", "tabular", "random", "minimax"]
    pairings = [
        ("dqn", "tabular"),
        ("dqn", "random"),
        ("dqn", "minimax"),
        ("tabular", "random"),
        ("tabular", "minimax"),
        ("random", "minimax"),
    ]

    def choose_action(agent_name, board, player):
        legal_moves = get_legal_moves(board)
        legal_actions = [
            row * 3 + col
            for row, col in legal_moves
        ]

        if not legal_actions:
            raise ValueError("No legal actions available")

        if agent_name == "dqn":
            state = encode_board_flat_length_nine(
                board,
                player,
            )

            legal_mask = np.zeros(9, dtype=bool)
            legal_mask[legal_actions] = True

            # Greedy evaluation: epsilon = 0.
            return dqn_select_action(
                online_params,
                state,
                legal_mask,
                0.0,
                rng,
            )

        if agent_name == "tabular":
            perspective_board = flip_board_perspective(
                board,
                player,
            )
            state_key = canonical_board_key(
                perspective_board
            )

            return greedy_argmax_over_legal_actions(
                q_table,
                state_key,
                legal_actions,
                rng,
            )

        if agent_name == "random":
            row, col = random_move_agent(
                board,
                player,
                rng,
            )
            return row * 3 + col

        if agent_name == "minimax":
            _, move = minimax_max_min_step(
                board,
                player,
            )

            if move is None:
                raise RuntimeError(
                    "Minimax returned no move on a nonterminal board"
                )

            row, col = move
            return row * 3 + col

        raise ValueError(f"Unknown agent: {agent_name}")

    results = {}

    for first_agent, second_agent in pairings:
        wins = 0
        losses = 0
        draws = 0

        for game_index in range(num_games):
            game = TicTacToeGame()

            # Alternate which agent plays X.
            if game_index % 2 == 0:
                x_agent = first_agent
                o_agent = second_agent
                first_agent_player = 1
            else:
                x_agent = second_agent
                o_agent = first_agent
                first_agent_player = -1

            while not game.is_terminal():
                current_agent = (
                    x_agent
                    if game.current_player == 1
                    else o_agent
                )

                action = choose_action(
                    current_agent,
                    game.board,
                    game.current_player,
                )

                row = action // 3
                col = action % 3
                game.step(row, col)

            if game.status == "draw":
                draws += 1
            elif (
                game.status == "X_win"
                and first_agent_player == 1
            ) or (
                game.status == "O_win"
                and first_agent_player == -1
            ):
                wins += 1
            else:
                losses += 1

        if num_games == 0:
            win_rate = 0.0
            loss_rate = 0.0
            draw_rate = 0.0
        else:
            win_rate = wins / num_games
            loss_rate = losses / num_games
            draw_rate = draws / num_games

        pairing_name = f"{first_agent}_vs_{second_agent}"

        results[pairing_name] = {
            "wins": win_rate,
            "losses": loss_rate,
            "draws": draw_rate,
        }

    return results

# Step 85 - sarsa_on_policy_update
def sarsa_on_policy_update(q_table, state_key, action, reward, next_state_key, next_action, done, alpha, gamma):
    """Apply one on-policy SARSA update and return the updated q_table."""
    # TODO: compute the SARSA TD target using the next action actually taken, then update Q(s, a).

    current_q = get_q_value(q_table, state_key, action)

    future_q = reward
    if not done:
        future_q += gamma * get_q_value(q_table, next_state_key, next_action) - current_q
    updated_q = current_q + alpha * future_q

    set_q_value(q_table, state_key, action, updated_q)

    return q_table

# Step 86 - train_sarsa_agent (not yet solved)
# TODO: implement

# Step 87 - reinforce_log_prob_of_action (not yet solved)
# TODO: implement

# Step 88 - reinforce_collect_episode_returns (not yet solved)
# TODO: implement

# Step 89 - reinforce_policy_gradient_update (not yet solved)
# TODO: implement

# Step 90 - train_reinforce_agent (not yet solved)
# TODO: implement

# Step 91 - compare_value_vs_policy_learners (not yet solved)
# TODO: implement

# Step 92 - symmetry_augmented_training (not yet solved)
# TODO: implement

