from typing import List


class Solution:
    def arraysIntersection(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        """
        [1213. Intersection of Three Sorted Arrays](https://www.cnblogs.com/Dylan-Java-NYC/p/12047372.html)

        Given three integer arrays `arr1`, `arr2` and `arr3` sorted in strictly increasing order,
        return a sorted array of only the integers that appeared in all three arrays.

        Example 1:

        ```
        Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
        Output: [1,5]
        Explanation: Only 1 and 5 appeared in the three arrays.
        ```

        Constraints:

        - 1 <= arr1.length, arr2.length, arr3.length <= 1000`

        - 1 <= arr1[i], arr2[i], arr3[i] <= 2000`

        """
        i, j, k = 0, 0, 0
        res = []

        while i < len(nums1) and j < len(nums2) and k < len(nums3):
            if nums1[i] == nums2[j] and nums2[j] == nums3[k]:
                res.append(nums1[i])
                i, j, k = i+1, j+1, k+1
            elif nums1[i] < nums2[j]:
                i = i + 1
            elif nums2[j] < nums3[k]:
                j = j + 1
            else:
                k = k + 1
        return res


