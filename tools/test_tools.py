import sys
sys.path.append("..")
from Arms import Arm
import unittest
import tools as t

class TestTools(unittest.TestCase):
    def test_best_arm(self):
        n = 10
        list_arm_idx = []
        for i in range(n):
            cur_arm = Arm.Arm(mu=0.5)
            cur_arm.idx = i
            list_arm_idx.append((cur_arm, i))
        self.assertEqual(t.best_arm(list_arm_idx).idx, n-1)

        list_arm_idx[n//2] = (list_arm_idx[n//2][0], n*10)
        self.assertEqual(t.best_arm(list_arm_idx).idx, n//2)

if __name__ == '__main__':
    unittest.main()
