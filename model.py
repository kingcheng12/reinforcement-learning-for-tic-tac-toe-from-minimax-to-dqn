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

# Step 51 - episode_apply_q_update (not yet solved)
# TODO: implement

# Step 52 - episode_check_terminate (not yet solved)
# TODO: implement

# Step 53 - train_q_learning_agent (not yet solved)
# TODO: implement

# Step 54 - compute_batched_outcome_stats (not yet solved)
# TODO: implement

# Step 55 - self_play_episode (not yet solved)
# TODO: implement

# Step 56 - flip_board_perspective (not yet solved)
# TODO: implement

# Step 57 - perspective_reward_sign (not yet solved)
# TODO: implement

# Step 58 - train_q_agent_self_play (not yet solved)
# TODO: implement

# Step 59 - evaluate_q_agent_vs_random (not yet solved)
# TODO: implement

# Step 60 - evaluate_q_agent_vs_minimax (not yet solved)
# TODO: implement

# Step 61 - inspect_q_values_for_state (not yet solved)
# TODO: implement

# Step 62 - serialize_q_table_to_dict (not yet solved)
# TODO: implement

# Step 63 - deserialize_q_table_from_dict (not yet solved)
# TODO: implement

# Step 64 - encode_board_flat_length_nine (not yet solved)
# TODO: implement

# Step 65 - encode_board_one_hot_length_eighteen (not yet solved)
# TODO: implement

# Step 66 - build_mlp_architecture (not yet solved)
# TODO: implement

# Step 67 - initialize_mlp_parameters (not yet solved)
# TODO: implement

# Step 68 - mlp_forward_pass (not yet solved)
# TODO: implement

# Step 69 - mask_illegal_actions_neg_inf (not yet solved)
# TODO: implement

# Step 70 - argmax_action_from_q_values (not yet solved)
# TODO: implement

# Step 71 - mse_loss_on_chosen_action (not yet solved)
# TODO: implement

# Step 72 - mlp_backward_pass (not yet solved)
# TODO: implement

# Step 73 - adam_update_step (not yet solved)
# TODO: implement

# Step 74 - create_replay_buffer (not yet solved)
# TODO: implement

# Step 75 - append_transition_to_buffer (not yet solved)
# TODO: implement

# Step 76 - cap_buffer_size_drop_oldest (not yet solved)
# TODO: implement

# Step 77 - sample_minibatch_from_buffer (not yet solved)
# TODO: implement

# Step 78 - build_target_network_copy (not yet solved)
# TODO: implement

# Step 79 - compute_target_q_with_target_network (not yet solved)
# TODO: implement

# Step 80 - sync_target_network_periodically (not yet solved)
# TODO: implement

# Step 81 - dqn_select_action (not yet solved)
# TODO: implement

# Step 82 - dqn_train_step (not yet solved)
# TODO: implement

# Step 83 - train_dqn_agent (not yet solved)
# TODO: implement

# Step 84 - compare_dqn_tabular_random_minimax (not yet solved)
# TODO: implement

# Step 85 - sarsa_on_policy_update (not yet solved)
# TODO: implement

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

