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

    def playGame(self):
<<<<<<< HEAD:Games/Game.py
        t = 0
        while t <= horizon - 1:
            arm_t, reward_t = self.policy.playArm(self.env,
                                                            self.mu_hat_history,
                                                            t)
=======
        t = 1
        while t <= self.horizon:
            arm_t, reward_t = self.policy.playArm(self.env, t)
>>>>>>> 5f951a5ba1624e28032593e4b9284d19f4f2d68d:Game/Game.py
            regret_t += self.opt_arm.mu - arm_t.mu


            arm_drawn_history.append(arm_t)
            regret_history.append(regret_t)
            leader_history.append(leader_t)



    def plot_and_save(self,
                      output_dir,
                      show_regret=True,
                      show_arm=True,
                      show_mu_hat=True):
        if show_regret:
            plt.figure()
            plt.plot(regret_history)
            plt.title("Regret history")
            plt.xlabel("t")
            plt.ylabel("Regret")
            plt.savefig(os.path.join(output_dir,"regret.jpg"))
        if show_arm:
            plt.figure()
            plt.plot(arm_drawn_history)
            plt.title("Arm drawn history")
            plt.xlabel("t")
            plt.ylabel("Arm drawn")
            plt.savefig(os.path.join(output_dir,"arm_drawn_history.jpg"))
        if show_mu_hat:
            mu_hat_matrix = np.zeros((self.env.nb_arms, self.horizon))
            for i, cur_arm in enumerate(self.env.list_of_arms):
                mu_hat_matrix[i,:] = cur_arm.mu_hat_history
            plt.imshow(mu_hat_matrix)
            plt.title("Mu hat history")
            plt.savefig(os.path.join(output_dir,"mu_hat_history.jpg"))
