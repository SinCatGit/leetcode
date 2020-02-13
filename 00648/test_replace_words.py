import unittest
from replace_words import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(
            'the cat was rat by the bat',
            sol.replaceWords(['cat', 'bat', 'rat'], 'the cattle was rattled by the battery')
        )

        self.assertEqual(
            'a a a a a a a a bbb baba a',
            sol.replaceWords(['a', 'aa', 'aaa', 'aaaa'], 'a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa')
        )


if __name__ == '__main__':
    unittest.main()
