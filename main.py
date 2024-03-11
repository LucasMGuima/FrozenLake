from gymnasium.envs.toy_text.frozen_lake import generate_random_map
import gymnasium as gym
from Agente import AgenteV1

env = gym.make("FrozenLake-v1", render_mode="human",  is_slippery=False,  desc=generate_random_map(size=8))
agent = AgenteV1(8)

observation, info = env.reset()

aprendendo = True
acoes = []
acoes_temp = []

while aprendendo:
    action = agent.get_action(observation)
    acoes_temp.append(action)
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        #informa o agente que terminou e em qual posição
        acoes = acoes_temp
        acoes_temp = []
        aprendendo = True if agent.terminated(observation) == False else False
        observation, info = env.reset()

print(acoes)
env.close()