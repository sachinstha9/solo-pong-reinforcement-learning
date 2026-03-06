import flappy_bird_gymnasium
import gymnasium
import torch
from dqn import DQN
from experience_replay import ReplayMemory
import itertools
import yaml

device = 'cuda' if torch.cuda.is_available() else 'cpu'

class Agent:
    def __init__(self, hyperparameter_set):
        with open('hyperparameters.yml') as file:
            all_hyperparamter_sets = yaml.safe_load(file)
            hyperparameters = all_hyperparamter_sets[hyperparameter_set]
        
        self.mini_batch_size = hyperparameters["mini_batch_size"]
        self.epsilon_init = hyperparameters["epsilon_init"]
        self.epsilon_decay = hyperparameters["epsilon_decay"]
        self.epsilon_min = hyperparameters["epsilon_min"]

    def run(self, is_training=True, render=True):
        env = gymnasium.make("FlappyBird-v0", render_mode="human" if render else None)

        num_states = env.observation_space.shape[0]
        num_actions = env.action_space.n

        policy_dqn = DQN(num_states, num_actions).to_device(device)

        if is_training:
            memory = ReplayMemory(100_000)

        reward_per_episode = []

        for episode in itertools.count():
            state, _ = env.reset()
            terminated = False
            episode_reward = 0.0

            while not terminated:
                action = env.action_space.sample()
                new_state, reward, terminated, _, info = env.step(action)

                episode_reward += reward

                if is_training:
                    memory.append((state, action, new_state, reward, terminated))

                state = new_state

            reward_per_episode.append(episode_reward)