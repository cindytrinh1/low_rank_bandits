import random
import numpy as np
import pickle
import matplotlib.pyplot as plt



def best_arm(list_arm_idx):
    """list_arm_idx = [(arm, ucb_idx),...]"""
    sorted_tuple = sorted(list_arm_idx,
      key=lambda x:x[1],
      reverse=True)
    optimal = True
    list_best_arms = [sorted_tuple[0][0]] # First arm of sorted tuple
    i = 0
    while optimal and i < len(sorted_tuple):
        if sorted_tuple[i][1] == sorted_tuple[0][1]:
            list_best_arms.append(sorted_tuple[i][0])
        else:
            optimal = False
    return random.choice(list_best_arms)
