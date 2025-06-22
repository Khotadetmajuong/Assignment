# Assignment One train RL agent to navigate to cross the road with actions right, left, right
import numpy as np
import random

#envt setup
road_length = 5 #the road will have 5 positions 0,4 is our reach position 4
actions = ['left','right'] #agent can take left and right

#Q-table initialisation
Q = np.zeros((road_length, len(actions))) #is core of Q-learning which intialise Q table

#hyperparameters
episodes = 1000 #number of training interactions , leads to better learning rates
learning_rate = 0.8 # btn 0 - 1 , alpha learning rate , helps agent to adapt more quickly
game = 0.9 #it will have a higher rewards
epsilon = 0.3 #helps agent to discover new paths # exploration rates
discount_factor = 0.9

#training loop
for episodes in range(episodes):
    state =  0 #start position 0

    while state != 4 :
        if random.uniform(0,1) < epsilon:
            actions = random.randint(0,1) # explore my random action 
        else:
            action = np.argmax(Q[state]) #explits the best known action

             # Determine next state
        if action == 0:  # Left
            next_state = max(0, state - 1)
        else:  # Right
            next_state = min(road_length - 1, state + 1)

        # Define reward
        if next_state == 4:
            reward = 1  # Reached goal
        else:
            reward = -0.01  # Small penalty to encourage faster path

        # Q-learning update rule
        Q[state, action] = Q[state, action] + learning_rate * (
            reward + discount_factor * np.max(Q[next_state]) - Q[state, action] # type: ignore
        )

        # Move to the next state
        state = next_state

# Display the learned Q-table
print("Trained Q-table:")
for i in range(road_length):
    print(f"Position {i}: Left = {Q[i][0]:.2f}, Right = {Q[i][1]:.2f}")     


