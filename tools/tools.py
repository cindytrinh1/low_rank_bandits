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



def single_arm_draw(mu,
                    horizon,
                    output_pickle=None,
                    law='Bernoulli',
                    plot=True):
    """
    draws_dict["draws_in_advance"] : (K, T)
    """
    mu_tile = np.tile(mu, (horizon, 1)).T
    draws_dict = {}
    draws_dict["mu"] = mu
    draws_dict["horizon"] = horizon
    draws_dict["draws_in_advance"] = np.random.binomial(1,mu_tile)
    if output_pickle:
        pickle.dump(draws_dict, open(output_pickle, 'wb'))
    if plot:
        plt.figure(figsize=(15,15))
        plt.imshow(draws_dict["draws_in_advance"], interpolation='nearest', aspect='auto')
        plt.colorbar()
        plt.show()
    return draws_dict

def pair_arm_draw(mu_row,
                  mu_col,
                  horizon,
                  output_pickle=None,
                  law='Bernoulli',
                  plot=True):
    nb_row, nb_col = len(mu_row), len(mu_col)
    total_pair_arms = nb_row * nb_col
    mu_matrix = np.dot(mu_row.reshape(nb_row,1), mu_col.reshape(1, nb_col))
    mu_flat = mu_matrix.flatten()
    return single_arm_draw(mu_flat, horizon, output_pickle, law, plot)


if __name__ == "__main__":
    horizon = 1000
    nb_row = 10
    nb_col = 10
    mu_row = np.linspace(0.1, 0.9, nb_row)
    mu_col = np.linspace(0.1, 0.9, nb_col)
    draws_dict = pair_arm_draw(mu_row,mu_col, horizon)
    draws = draws_dict["draws_in_advance"]
