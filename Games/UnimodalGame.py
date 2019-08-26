import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append("..")
from Games.Game import Game
class UnimodalGame(Game):
    def __init__(self,
                environment,
                policy,
                horizon=20000):

        super().__init__(self,
                        environment,
                        policy,
                        horizon)

        assert self.environment.isinstanceof(UnimodalEnvironment)
        assert self.policy.isUnimodalPolicy

        self.leader_history = []


    def playGame(self):
        t = 0
        while t < horizon:
            arm_t, reward_t, leader_t = self.policy.playArm(self.env,
                                                            t)
            regret_t += self.opt_arm.mu - arm_t.mu


            arm_drawn_history.append(arm_t)
            regret_history.append(regret_t)
            leader_history.append(leader_t)
        print(arm_drawn_history)
        print(regret_history)
        print(leader_history)



    # def plot_and_save(self,
    #                   output_dir,
    #                   show_regret=True,
    #                   show_leader=True,
    #                   show_arm=True):
    # ## plot leader
