import argparse
import matplotlib.pyplot as plt
import numpy as np


from Games import utils_draws as ud
from Games import UnimodalGame as ug

from Environments import Rank1Env as r1e
from Policies import OSUB

if __name__ == "__main__":
    ## Parameters
    output_dir = "./results"

    horizon = 500
    nb_row = 5
    nb_col = 5
    mu_row = np.linspace(0.1, 0.9, nb_row)
    mu_col = np.linspace(0.1, 0.9, nb_col)


    ## Draws in advance

    draws_dict = ud.pair_arm_draw(mu_row=mu_row,
                      mu_col=mu_col,
                      horizon=horizon,
                      output_pickle=None,
                      law='Bernoulli',
                      plot=False)
    draws_in_advance = draws_dict["draws_in_advance"]


    ## Create Environment
    print("Create environment")
    my_rank1_env = r1e.create_rank1env(mu_row, mu_col, draws_in_advance)
    print("mu matrix", my_rank1_env.mu_matrix)

    ## Launch game
    my_policy = OSUB.OSUB(draw_leader_every=5)
    osub_game = ug.UnimodalGame(environment=my_rank1_env,
                                policy=my_policy,
                                draws_in_advance=draws_in_advance,
                                horizon=horizon)
    #
    # my_policy = OSUB.OSUB(draw_leader_every=5)
    # osub_game = ug.UnimodalGame(environment=my_rank1_env,
    #                             policy=my_policy,
    #                             draws_in_advance=draws_in_advance)
    #
    # osub_game.playGame()
