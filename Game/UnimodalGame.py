import matplotlib.pyplot as plt
import numpy as np

class UnimodalGame(Game):
    def __init__(self,
                environment,
                policy,
                draws_in_advance,
                horizon=20000):

        super().__init__(self,
                        environment,
                        policy,
                        draws_in_advance,
                        horizon=20000)

        assert self.environment.isinstanceof(UnimodalEnvironment)
        assert self.policy.isUnimodalPolicy


        self.leader_history = []


    def plot_leader():
        pass
