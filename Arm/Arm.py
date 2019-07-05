import numpy as np
class Arm:
    def __init__(self,
                idx,
                mu,
                draws_in_advance=None,
                law="Bernoulli"):
        self.idx = idx
        self.mu = mu
        self.law = law
        self.draws_in_advance = draws_in_advance
        self.mu_hat = 0
        self.mu_hat_history = []
        self.nb_times_drawn = 0

    def draw(self, t):
        if self.draws_in_advance != None:
            reward = self.draws_in_advance[t]

        elif law == 'Bernoulli':
            reward = np.random(0, self.mu)
        self.mu_hat =
        self.mu_hat_history.append(self.mu_hat)
        self.nb_times_drawn += 1


        return reward




class PairArm(Arm):
    def __init__(self, idx, mu, idx_row, idx_col, law="Bernoulli"):
        super().__init__(idx, mu, law)
        self.idx_row = idx_row
        self.idx_col = idx_col
