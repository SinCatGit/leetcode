import unittest
from design_phone_directory import PhoneDirectory


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        pd = PhoneDirectory(3)
        self.assertEqual(0, pd.get())
        self.assertEqual(1, pd.get())
        self.assertTrue(pd.check(2))
        self.assertEqual(2, pd.get())
        self.assertFalse(pd.check(2))
        pd.release(2)
        self.assertTrue(pd.check(2))


if __name__ == '__main__':
    unittest.main()
