import unittest
from reconstruct_itinerary import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()
        self.assertEqual(
            ['JFK', 'MUC', 'LHR', 'SFO', 'SJC'],
            solution.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))

        self.assertEqual(
            ['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO'],
            solution.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))

        self.assertEqual(
            ['JFK', 'NRT', 'JFK', 'KUL'],
            solution.findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]))

        self.assertEqual(
            ["JFK", "AXA", "AUA", "ADL", "ANU", "AUA", "ANU", "EZE", "ADL", "EZE", "ANU", "JFK", "AXA", "EZE", "TIA",
             "AUA", "AXA", "TIA", "ADL", "EZE", "HBA"],
            solution.findItinerary([["EZE", "TIA"], ["EZE", "HBA"], ["AXA", "TIA"], ["JFK", "AXA"], ["ANU", "JFK"],
                                    ["ADL", "ANU"], ["TIA", "AUA"], ["ANU", "AUA"], ["ADL", "EZE"], ["ADL", "EZE"],
                                    ["EZE", "ADL"], ["AXA", "EZE"], ["AUA", "AXA"], ["JFK", "AXA"], ["AXA", "AUA"],
                                    ["AUA", "ADL"], ["ANU", "EZE"], ["TIA", "ADL"], ["EZE", "ANU"], ["AUA", "ANU"]]))

        self.assertEqual(
            ['JFK', 'MUC', 'LHR', 'SFO', 'SJC'],
            solution.findItineraryV01([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))

        self.assertEqual(
            ['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO'],
            solution.findItineraryV01([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))

        self.assertEqual(
            ['JFK', 'NRT', 'JFK', 'KUL'],
            solution.findItineraryV01([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]))

        self.assertEqual(
            ["JFK", "AXA", "AUA", "ADL", "ANU", "AUA", "ANU", "EZE", "ADL", "EZE", "ANU", "JFK", "AXA", "EZE", "TIA",
             "AUA", "AXA", "TIA", "ADL", "EZE", "HBA"],
            solution.findItineraryV01([["EZE", "TIA"], ["EZE", "HBA"], ["AXA", "TIA"], ["JFK", "AXA"], ["ANU", "JFK"],
                                    ["ADL", "ANU"], ["TIA", "AUA"], ["ANU", "AUA"], ["ADL", "EZE"], ["ADL", "EZE"],
                                    ["EZE", "ADL"], ["AXA", "EZE"], ["AUA", "AXA"], ["JFK", "AXA"], ["AXA", "AUA"],
                                    ["AUA", "ADL"], ["ANU", "EZE"], ["TIA", "ADL"], ["EZE", "ANU"], ["AUA", "ANU"]]))


if __name__ == '__main__':
    unittest.main()
