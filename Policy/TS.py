import numpy as np

class TS(Policy):

    def playArm(env,
                mu_hat_history,
                t):
        nb_arms = env.nb_arms
        
