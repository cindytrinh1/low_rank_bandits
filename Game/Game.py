class Game:
    def __init__(self, environment, policy, horizon=20000):
        # game settings
        self.env = environment
        self.opt_arm = environment.opt_arm


        self.policy = policy
        self.horizon = horizon



        # history
        self.regret_history = []
        self.arm_drawn_history = []
        self.leader_history = [] # stay [] if no leader


    def playGame(self):
        t = 1
        while t <= horizon:
            arm_t, reward_t, leader_t = self.policy.playArm(self.env, t)
            regret_t = self.opt_arm.mu - arm_t.mu
            
            arm_drawn_history.append(arm_t)
            leader_history.append(leader_t)
