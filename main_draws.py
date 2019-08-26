import argparse
import matplotlib.pyplot as plt
import numpy as np
import os

from Games import utils_draws as ud
from Games import UnimodalGame as ug

from Environments import Rank1Env as r1e
from Policies import OSUB

def draws_advance_pair(nb_row, nb_col, horizon, output_folder):
    mu_row = np.linspace(0.1, 0.9, nb_row)
    mu_col = np.linspace(0.1, 0.9, nb_col)
    draws_dict = ud.pair_arm_draw(mu_row=mu_row,
                      mu_col=mu_col,
                      horizon=horizon,
                      output_pickle=os.path.join(output_folder, f'pair_row-{nb_row}_col-{nb_col}_horizon-{horizon}.p'),
                      law='Bernoulli',
                      plot=False)

if __name__ == "__main__":
    ## Parameters
    output_folder = "./results/draws"

    horizons = [1000, 10000, 30000, 50000]
    nb_row = [3, 5, 10, 20]
    nb_col = [3, 5, 10, 20]

    for h in horizons:
        for r in nb_row:
            for c in nb_col:
                draws_advance_pair(r, c, h, output_folder)
