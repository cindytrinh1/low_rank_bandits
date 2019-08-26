import matplotlib.pyplot as plt
import numpy as np
import os
import pickle as p

class Game:
    def __init__(self,
                environment,
                policy,
                horizon):
        # game settings
        self.env = environment
        self.opt_arm = self.env.opt_arm

        self.policy = policy
        self.horizon = horizon

        # history
        self.arm_drawn_history = []
        self.regret_history = []

    def playGame(self):
        t = 0
        regret_t = 0
        while t < self.horizon:
            arm_t, reward_t = self.policy.playArm(self.env,
                                                            t)
            regret_t += self.opt_arm.mu - arm_t.mu


            self.arm_drawn_history.append(arm_t)
            self.regret_history.append(regret_t)
            t += 1



    def plot_and_save(self,
                      output_dir,
                      show_regret=True,
                      show_arm=True,
                      show_mu_hat=True,
                      save_game=True):
        if show_regret:
            plt.figure()
            plt.plot(self.regret_history)
            plt.title("Regret history")
            plt.xlabel("t")
            plt.ylabel("Regret")
            plt.savefig(os.path.join(output_dir,f"{self.policy.name}_regret_horizon-{self.horizon}.jpg"))
        if show_arm:
            plt.figure()
            plt.subplot(121)
            idx_arm_drawn_history = [cur_arm.idx for cur_arm in self.arm_drawn_history]
            plt.plot(np.arange(self.horizon), idx_arm_drawn_history, 'r*')
            plt.title("Arm drawn history")
            plt.xlabel("t")
            plt.ylabel("idx arm drawn")

            plt.subplot(122)
            mu_arm_drawn_history = [cur_arm.mu for cur_arm in self.arm_drawn_history]
            plt.plot(np.arange(self.horizon), mu_arm_drawn_history, 'r*')
            plt.title("Arm drawn history")
            plt.xlabel("t")
            plt.ylabel("mu arm drawn")

            plt.savefig(os.path.join(output_dir,f"{self.policy.name}_arm_drawn_history_horizon-{self.horizon}.jpg"))
        if show_mu_hat:
            plt.figure()
            mu_hat_matrix = np.zeros((self.env.nb_arms, self.horizon))
            for i, cur_arm in enumerate(self.env.list_of_arms):
                mu_hat_matrix[i,:] = cur_arm.mu_hat_history + [0 for i in range(len(cur_arm.mu_hat_history), self.horizon)]
            plt.imshow(mu_hat_matrix,interpolation='nearest', aspect='auto')
            plt.colorbar()
            plt.title("Mu hat history")
            plt.savefig(os.path.join(output_dir,f"{self.policy.name}mu_hat_history_horizon-{self.horizon}.jpg"))

        if save_game:
            with open(os.path.join(output_dir,f"{self.policy.name}_game.p"), 'wb') as f:
                p.dump(self, f)
