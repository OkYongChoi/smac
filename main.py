'''
Algorithm setting method: algorithm = config/algs 
E.g.
QMIX of rnn agent: algorithm = 'RNN_AGENT/qmix_beta'
COMA of G2ANet agent: algorithm = 'G2ANet_Agent/coma'

Mini game setting method: refer to the envs/starcraft2/maps/smac_maps.py
Description:
3 marines vs 3 marines: minigame = '3m'
2 zealots 3 stalkers vs 2 zealots 3 stalkers -> '2s3z'
'''

import numpy as np
import torch as th
from utils.logging import get_logger
import random
from run import standard_run
from offpg_run import offpg_run
import config_util as cu




if __name__ == '__main__':
    logger = get_logger()
    
    algorithm = 'RNN_AGENT/qmix'
    minigame = '3s_vs_5z'

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