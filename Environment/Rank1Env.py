import numpy as np
class Rank1Env(UnimodalEnvironment):
    def __init__(self, mu_row, mu_col):
        self.mu_row = mu_row # list of row means ("u")
        self.nb_row = len(mu_row)
        self.mu_col = mu_col # "v"
        self.nb_col = len(mu_col)
        self.mu_matrix = np.dot(self.mu_row.reshape(self.nb_row,1),self.mu_col.reshape(1,self.nb_col))
        self.mu_flat = self.mu_matrix.flatten()
        ## Create list_of_pair_arms
        super().__init__(list_of_pair_arms)

        ## Create self.matrix_arms?



    def get



    def getNeighbors(arm,
                    arm_included=True):
        list_of_neighbors = []
        return list_of_neighbors
