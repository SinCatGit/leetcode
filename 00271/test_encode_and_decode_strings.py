import unittest
from encode_and_decode_strings import Codec


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Codec()
        self.assertEqual(
            ['lint', 'code', 'love', 'you'],
            sol.decode(sol.encode(['lint', 'code', 'love', 'you']))
        )
        self.assertEqual(
            ['lint', 'code', '', 'you'],
            sol.decode(sol.encode(['lint', 'code', '', 'you']))
        )

        self.assertEqual(
            ['lint', 'c/ode', '', 'you'],
            sol.decode(sol.encode(['lint', 'c/ode', '', 'you']))
        )

        self.assertEqual(
            ['/lint/', 'c//ode', '', '/'],
            sol.decode(sol.encode(['/lint/', 'c//ode', '', '/']))
        )


if __name__ == '__main__':
    unittest.main()
