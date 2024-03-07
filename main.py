from gymnasium.envs.toy_text.frozen_lake import generate_random_map
import gymnasium as gym
from Agente import AgenteV1

env = gym.make("FrozenLake-v1", render_mode="human",  is_slippery=False,  desc=generate_random_map(size=8))
agent = AgenteV1(8)

observation, info = env.reset()

for _ in range(1000):
    action = agent.get_action(observation)
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated:
        #informa o agente que terminou e em qual posição
        agent.terminated(observation)

    if terminated or truncated:
        observation, info = env.reset()

env.close()