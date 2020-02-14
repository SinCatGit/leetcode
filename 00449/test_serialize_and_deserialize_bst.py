import unittest
from serialize_and_deserialize_bst import Codec, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Codec()
        self.assertEqual(
            '1 2 4 # # # 3 2 4 # # # 4 # #',
            sol.serialize(sol.deserialize('1 2 4 # # # 3 2 4 # # # 4 # #'))
        )


if __name__ == '__main__':
    unittest.main()
