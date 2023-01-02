import numpy as np

def game_of_life(state):
    # compute the number of live neighbors for each cell
    neighbors = (state[:, :] + state[:, 1:] + state[:, 2:] +
                state[1:, :] + state[1:, 2:] + state[2:, :] +
                state[2:, 1:] + state[2:, 2:])
    # apply the rules of the game
    state = ((neighbors == 3) | (state & (neighbors == 2)))
    return state

# initialize the game state
state = np.random.randint(0, 2, size=(50, 50))

# run the game for 10 steps
for i in range(10):
    state = game_of_life(state)
