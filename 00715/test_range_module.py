import unittest
from range_module import RangeModule, RangeModuleV01


class TestSolution(unittest.TestCase):
    def test_TwoSum_Solution(self):
        r = RangeModule()
        r.addRange(10, 180)
        self.assertEqual([(10, 180)], r.ranges)
        r.addRange(150, 200)
        self.assertEqual([(10, 200)], r.ranges)
        r.addRange(250, 500)
        self.assertEqual([(10, 200), (250, 500)], r.ranges)
        self.assertTrue(r.queryRange(50, 100))
        self.assertFalse(r.queryRange(180, 300))
        self.assertFalse(r.queryRange(600, 1000))
        r.removeRange(50, 150)
        self.assertEqual([(10, 50), (150, 200), (250, 500)], r.ranges)
        self.assertFalse(r.queryRange(50, 100))

        r = RangeModuleV01()
        r.addRange(10, 180)
        self.assertEqual([10, 180], r._X)
        r.addRange(150, 200)
        self.assertEqual([10, 200], r._X)
        r.addRange(250, 500)
        self.assertEqual([10, 200, 250, 500], r._X)
        self.assertTrue(r.queryRange(50, 100))
        self.assertFalse(r.queryRange(180, 300))
        self.assertFalse(r.queryRange(600, 1000))
        r.removeRange(50, 150)
        self.assertEqual([10, 50, 150, 200, 250, 500], r._X)
        self.assertFalse(r.queryRange(50, 100))


if __name__ == '__main__':
    unittest.main()
