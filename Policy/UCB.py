import numpy as np

class UCB(Policy):

    def playArm(env,
                mu_hat_history,
                t):
        nb_arms = env.nb_arms

        if t <= nb_arms:
            arm_t = env.get_arm_idx(t)
        else:
        	UCB_indexes = []
        	for cur_arm in env.list_of_arms:
        		UCB_indexes.append((cur_arm,
        							UCB1_idx(cur_arm, t)))
        	arm_t = tools.best_arm(UCB_indexes)
        reward = arm_t.draw(t)
        
        return arm_t, reward
        	
       
    def UCB1_idx(self,
    			  arm,
    			  t):
    	return arm.mu_hat + np.sqrt((2*np.log(t))/arm.nb_times_drawn)