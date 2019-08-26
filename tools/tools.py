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
    i = 1
    while optimal and i < len(sorted_tuple):
        if sorted_tuple[i][1] == sorted_tuple[0][1]:
            list_best_arms.append(sorted_tuple[i][0])
        else:
            optimal = False
        i += 1
    return random.choice(list_best_arms)


def klBern(x, y):
    """Kullback-Leibler divergence for Bernoulli distributions."""
    eps = 1e-15
    x = min(max(x, eps), 1-eps)
    y = min(max(y, eps), 1-eps)
    return x*np.log(x/y) + (1-x)*np.log((1-x)/(1-y))

def klucb(x, d, div, upperbound, lowerbound=-float('inf'), precision=1e-2):
    """The generic klUCB index computation.

    Input args.: x, d, div, upperbound, lowerbound=-float('inf'), precision=1e-6,
    where div is the KL divergence to be used.

    finds argmax_{q \in [x,upperbound]} (div(x,q) <= d)

    """
    l = max(x, lowerbound)
    u = upperbound
    while u-l>precision:
        m = (l+u)/2
        if div(x, m)>d:
            u = m
        else:
            l = m
    return (l+u)/2
