import argparse
import matplotlib.pyplot as plt
import numpy as np
import pickle as p
import os


from Games import utils_draws as ud
from Games import UnimodalGame as ug

from Environments import Rank1Env as r1e
from Policies import OSUB
from Policies import UTS



if __name__ == "__main__":
    ## Parameters
    draws_dir = "./results/draws"
    horizon = 10000
    nb_row = 3
    nb_col = 3
    results_dir = f"./results/pair_row-{nb_row}_col-{nb_col}_horizon-{horizon}"
    if not os.path.exists(results_dir):
        os.mkdir(results_dir)

    ## Load draws in advance
    pair_draw_pickle = f'pair_row-{nb_row}_col-{nb_col}_horizon-{horizon}.p'
    with open(os.path.join(draws_dir, pair_draw_pickle), 'rb') as f:
        draws_dict = p.load(f)
    draws_in_advance = draws_dict["draws_in_advance"]



    list_draw_leader_every = [3,5]
    regrets_OSUB = []
    regrets_UTS = []
    for draw_leader_every in list_draw_leader_every:
        output_dir = os.path.join(results_dir, f'draw_leader_every_{draw_leader_every}')
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

        ## OSUB
        OSUB_rank1_env = r1e.create_rank1env(draws_dict)
        OSUB_policy = OSUB.OSUB(draw_leader_every=draw_leader_every)
        osub_game = ug.UnimodalGame(environment=OSUB_rank1_env,
                                    policy=OSUB_policy,
                                    horizon=horizon)
        osub_game.playGame()
        osub_game.plot_and_save(output_dir=output_dir,
                                show_regret=True,
                                show_arm=True,
                                show_mu_hat=True,
                                show_leader=True,
                                save_game=True)
        regrets_OSUB.append(osub_game.regret_history)

        ## UTS
        UTS_rank1_env = r1e.create_rank1env(draws_dict)
        UTS_policy = UTS.UTS(draw_leader_every=draw_leader_every)
        UTS_game = ug.UnimodalGame(environment=UTS_rank1_env,
                                    policy=UTS_policy,
                                    horizon=horizon)
        UTS_game.playGame()
        UTS_game.plot_and_save(output_dir=output_dir,
                                show_regret=True,
                                show_arm=True,
                                show_mu_hat=True,
                                show_leader=True,
                                save_game=True)
        regrets_UTS.append(UTS_game.regret_history)


    plt.figure(figsize=(10,10))
    
