import matplotlib.pyplot as plt
import numpy as np

class Game:
    def __init__(self,
                environment,
                policy,
                horizon=20000):
        # game settings
        self.env = environment
        self.opt_arm = environment.opt_arm

        self.policy = policy
        self.horizon = horizon

        # history
        self.arm_drawn_history = []
        self.regret_history = []
        self.mu_hat_history = []

    def playGame(self):
        t = 1
        while t <= horizon:
            arm_t, reward_t, leader_t = self.policy.playArm(self.env,
                                                            self.mu_hat_history,
                                                            t)
            regret_t = self.opt_arm.mu - arm_t.mu


            arm_drawn_history.append(arm_t)
            regret_history.append(regret_t)
            leader_history.append(leader_t)



    def plot_and_save(self,
                      output_dir,
                      show_regret=True,
                      show_leader=True,
                      show_arm=True):
