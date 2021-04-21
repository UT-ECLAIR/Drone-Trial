from gym_pybullet_drones.envs.single_agent_rl.BaseSingleAgentAviary import ObservationType, ActionType
from track import TrackV1
import numpy as np
from gym_pybullet_drones.utils.Logger import Logger

# Create the environment
gui = True
obs = ObservationType.RGB # Define what type of observation your agent should intake, see README for details
act = ActionType.RPM # Define what type of action your agent should instake, see README for details
env = TrackV1(gui=gui, obs=obs, act=act)

# Obtain the PyBullet Client ID from the environment
PYB_CLIENT = env.getPyBulletClient()
# Now you can loop through it like any other gym environment, see below

# Logger to track stats
logger = Logger(logging_freq_hz=int(env.SIM_FREQ / env.AGGR_PHY_STEPS), num_drones=1)

# Training Algorithm
num_training_episodes = 1
obs = env.reset()
for episode in range(1, num_training_episodes + 1):
    done = False
    steps_per_episode = 0
    while not done:
        action = np.array([0.0, 0.0, 0.3, 0.3]) # TODO Implement your action, hopefully backed by RL
        obs, reward, done, info = env.step(action)
        logger.log(drone=0, timestamp=env.step_counter, state=env._getDroneStateVector(0))
        steps_per_episode += 1
        if done:
            obs = env.reset()
            print(episode)

env.close()
# save .npy arrays to logs directory
logger.save()
# save csv information to desktop, comment out/delete if you don't want this
logger.save_as_csv("trial")
# plot the data on a graph
logger.plot()