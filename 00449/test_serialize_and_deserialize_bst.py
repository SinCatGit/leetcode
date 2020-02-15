import unittest
from serialize_and_deserialize_bst import Codec


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Codec()
        self.assertEqual(
            '2 1 3',
            sol.serialize(sol.deserialize('2 1 3'))
        )


if __name__ == '__main__':
    unittest.main()
