import unittest
from serialize_and_deserialize_n_ary_tree import Codec


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Codec()
        #     1
        #   / | \
        #  3  2  4
        # / \
        # 5  6
        self.assertEqual('1 3 5 # 6 # # 2 # 4 # #', sol.serialize(sol.deserialize('1 3 5 # 6 # # 2 # 4 # #')))
        self.assertEqual('1 3 5 # 6 # # 2 # 4 # #', sol.serialize(sol.deserializeV01('1 3 5 # 6 # # 2 # 4 # #')))
        self.assertEqual('1 3 3 2 5 0 6 0 2 0 4 0', sol.serializeV02(sol.deserializeV02('1 3 3 2 5 0 6 0 2 0 4 0')))


if __name__ == '__main__':
    unittest.main()
