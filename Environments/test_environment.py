import unittest
import numpy as np
import Rank1Env as r1e
import pickle as p
import sys
sys.path.append("../")
from Arms.Arm import PairArm

class TestEnvironment(unittest.TestCase):
    def test_create_r1env_advance(self):
        mu_row = np.linspace(0.1, 0.5, 5)
        mu_col = np.linspace(0.1, 0.3, 3)
        nb_row = len(mu_row)
        nb_col = len(mu_col)
        with open('../test_folder/pair_draw_1000.p', 'rb') as f:
            draws_dict = p.load(f)
        draws_in_advance = draws_dict['draws_in_advance']
        my_rank1_env = r1e.create_rank1env(mu_row, mu_col, draws_in_advance)
        self.assertEqual(my_rank1_env.nb_arms, nb_row*nb_col)
        self.assertTrue((my_rank1_env.mu_row == mu_row).all())
        self.assertTrue((my_rank1_env.mu_col == mu_col).all())
        self.assertTrue((my_rank1_env.mu_matrix == np.dot(mu_row.reshape(nb_row,1), mu_col.reshape(1, nb_col))).all())
        self.assertTrue((my_rank1_env.mu_flat == my_rank1_env.mu_matrix.flatten()).all())
        self.assertTrue((len(my_rank1_env.list_of_arms) == nb_row*nb_col))
        self.assertIsInstance(my_rank1_env.list_of_arms[0], PairArm)

        # Check idx of arms
        list_idx_arms = set()
        for cur_arm in my_rank1_env.list_of_arms:
            self.assertTrue(0 <= cur_arm.idx < my_rank1_env.nb_arms)
            self.assertTrue(0 <= cur_arm.idx_pair[0] < nb_row)
            self.assertTrue(0 <= cur_arm.idx_pair[1] < nb_col)

            list_idx_arms.add(cur_arm.idx)
        self.assertEqual(len(list_idx_arms), my_rank1_env.nb_arms)

    def test_get_arm_idx(self):
        mu_row = np.linspace(0.1, 0.5, 5)
        mu_col = np.linspace(0.1, 0.3, 3)
        nb_row = len(mu_row)
        nb_col = len(mu_col)
        with open('../test_folder/pair_draw_1000.p', 'rb') as f:
            draws_dict = p.load(f)
        draws_in_advance = draws_dict['draws_in_advance']
        my_rank1_env = r1e.create_rank1env(mu_row, mu_col, draws_in_advance)

        idx_0 = (0, 0)
        arm_0 = my_rank1_env.get_arm_idx(idx_0)
        self.assertEqual(my_rank1_env.get_arm_idx(0), arm_0)
        self.assertIsInstance(arm_0, PairArm)
        self.assertEqual(arm_0.mu, 0.1*0.1)
        self.assertEqual(arm_0.idx, 0)
        self.assertEqual(arm_0.idx_pair, (0,0))
        self.assertEqual(arm_0.idx_row, 0)
        self.assertEqual(arm_0.idx_col, 0)
        my_rank1_env.set_neighbors(arm=arm_0)
        neighbors_0_mu = []
        for j, mu_j in enumerate(mu_col):
            neighbors_0_mu.append(0.1*mu_j)
        for i, mu_i in enumerate(mu_row):
            neighbors_0_mu.append(mu_i*0.1)
        for cur_neighbor in arm_0.neighbors:
            self.assertTrue(cur_neighbor.mu in neighbors_0_mu)

        idx_8 = 8
        arm_8 = my_rank1_env.get_arm_idx(idx_8)
        self.assertIsInstance(arm_8, PairArm)
        self.assertTrue(abs(arm_8.mu - 0.3*0.3) < 1e-5)
        self.assertEqual(arm_8.idx, 8)
        self.assertEqual(arm_8.idx_pair, (2,2))
        self.assertEqual(arm_8.idx_row, 2)
        self.assertEqual(arm_8.idx_col, 2)


    def test_set_neighbors(self):
        mu_row = np.linspace(0.1, 0.5, 5)
        mu_col = np.linspace(0.1, 0.3, 3)
        nb_row = len(mu_row)
        nb_col = len(mu_col)
        with open('../test_folder/pair_draw_1000.p', 'rb') as f:
            draws_dict = p.load(f)
        draws_in_advance = draws_dict['draws_in_advance']
        my_rank1_env = r1e.create_rank1env(mu_row, mu_col, draws_in_advance)

        list_idx_arms = set()
        for cur_arm in my_rank1_env.list_of_arms:
            self.assertTrue(0 <= cur_arm.idx < my_rank1_env.nb_arms)
            list_idx_arms.add(cur_arm.idx)
        self.assertEqual(len(list_idx_arms), my_rank1_env.nb_arms)

        idx_0 = (0, 0)
        arm_0 = my_rank1_env.get_arm_idx(idx_0)
        my_rank1_env.set_neighbors(arm=arm_0)
        neighbors_0_mu = []
        for j, mu_j in enumerate(mu_col):
            neighbors_0_mu.append(0.1*mu_j)
        for i, mu_i in enumerate(mu_row):
            neighbors_0_mu.append(mu_i*0.1)
        for cur_neighbor in arm_0.neighbors:
            self.assertTrue(cur_neighbor.mu in neighbors_0_mu)

        idx_8 = 8
        arm_8 = my_rank1_env.get_arm_idx(idx_8)
        my_rank1_env.set_neighbors(arm=arm_8)
        neighbors_8_mu = []
        for j, mu_j in enumerate(mu_col):
            neighbors_8_mu.append(0.3*mu_j)
        for i, mu_i in enumerate(mu_row):
            neighbors_8_mu.append(mu_i*0.3)
        for cur_neighbor in arm_8.neighbors:
            self.assertTrue(cur_neighbor.mu in neighbors_8_mu)

        self.assertEqual(len(arm_8.neighbors), nb_row + nb_col - 1)



if __name__ == '__main__':
    unittest.main()
