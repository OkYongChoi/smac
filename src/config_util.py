'''
    Get all of the configuration such as about
    envs, algos, etc.
'''

import collections
from copy import deepcopy
import yaml

def recursive_dict_update(d, u):
    """Add all of the items of u into the d"""
    for k, v in u.items():
        if isinstance(v, collections.Mapping):
            d[k] = recursive_dict_update(d.get(k, {}), v)
        else:
            d[k] = v
    return d


def get_config(algorithm, minigame):
    
    with open("config/envs/sc2_beta.yaml", "r") as f:
        try:
            config_envs_dict = yaml.load(f, Loader=yaml.SafeLoader)
        except yaml.YAMLError as exc:
            assert False, f"sc2.yaml error: {exc}"
        env_config = config_envs_dict

    with open("config/default.yaml","r") as f:
        try:
            default_config = yaml.load(f, Loader=yaml.SafeLoader)
        except yaml.YAMLError as exc:
            assert False, f"default.yaml error: {exc}"

    # The below block depends on each algorithm    
    with open(f"config/algs/{algorithm}.yaml", "r") as f:
        try:
            config_algs_dict = yaml.load(f, yaml.SafeLoader)
        except yaml.YAMLError as exc:
            assert False, f"sc2.yaml error: {exc}"
        alg_config = config_algs_dict

    final_config_dict = recursive_dict_update(default_config, env_config)
    final_config_dict = recursive_dict_update(final_config_dict, alg_config)

    final_config_dict['env_args']['map_name'] = minigame

    return final_config_dict
    
def config_copy(config):
    if isinstance(config, dict):
        return {k: config_copy(v) for k, v in config.items()}
    elif isinstance(config, list):
        return [config_copy(v) for v in config]
    else:
        return deepcopy(config)
