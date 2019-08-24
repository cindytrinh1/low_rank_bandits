import numpy as np
import Arm
import Environment as env
from Environment import Rank1Env as r1e
import Game.Game as g
import Policy as p
import Policy.OSUB as testOSUB
import tools.tools as t
import argparse
import matplotlib.pyplot as plt

if __name__ == "__main__":
    ## Parameters
    output_dir = "./results"

    horizon = 1000
    nb_row = 5
    nb_col = 5
    mu_row = np.linspace(0.1, 0.9, nb_row)
    mu_col = np.linspace(0.1, 0.9, nb_col)


    draws_dict = t.pair_arm_draw(mu_row, mu_col, horizon)
    draws_in_advance = draws_dict["draws_in_advance"]


    ## Create Environment
    my_rank1_env = r1e.create_rank1env(mu_row,mu_col, draws_in_advance)

    ## Launch game
    my_policy = testOSUB.OSUB(draw_leader_every=5)
    osub_game = g.Game(my_rank1_env, my_policy, horizon)
    osub_game.playGame()
