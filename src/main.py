import numpy as np
import torch as th
from utils.logging import get_logger
import random
from run import standard_run, offpg_run
import config_util as cu
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Choose algorithms from config/algs 
    parser.add_argument('--algorithm','-a', default = 'RNN_AGENT/qmix')
    # Refer to the envs/starcraft2/maps/smac_maps.py for the map setting
    parser.add_argument('--game', '-g', default = '2s3z')
    args = parser.parse_args()
    
    logger = get_logger()

    algorithm = args.algorithm
    minigame = args.game

    # Get all of the configuration such as maps, algorithms, hyper parameters, etc.
    config = cu.config_copy(cu.get_config(algorithm, minigame))

    random_Seed = random.randrange(0, 16546)
    np.random.seed(random_Seed)
    th.manual_seed(random_Seed)
    config['env_args']['seed'] = random_Seed

    is_offpg = config['off_pg']

    if is_offpg:
        offpg_run(config, logger, minigame)
    else:
        standard_run(config, logger, minigame)