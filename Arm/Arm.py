import numpy as np
class Arm:
    def __init__(self, idx, mu, law="Bernoulli"):
        self.idx = idx
        self.mu = mu
        self.law = law

    def draw():
        return reward



class PairArm(Arm):
    def __init__(self, idx, mu, idx_row, idx_col, law="Bernoulli"):
        super().__init__(idx, mu, law)
        self.idx_row = idx_row
        self.idx_col = idx_col
