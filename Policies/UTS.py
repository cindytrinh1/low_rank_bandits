class UTS(Policy):
    def __init__(self, draw_leader_every=None):
        self.draw_leader_every = draw_leader_every
        if draw_leader_every==None:
            pass

    def playArm(game, t):
        return arm, reward, leader
