"""
url:
https://leetcode.com/problems/two-sum/

"""

class Solution:
    def twoSum(self, nums, target):
        """
        This ia a naive brute force solution.
        Time complexity: O(n^2)
        Space complexity: O(1)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


class SolutionFaster:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        data = {}

        for index, value in enumerate(nums):
            if data.get(value) is None:
                data[value] = index
            if data.get(target - value) is not None and data[target - value] != index:
                return sorted([index, data[target - value]])


if __name__ == '__main__':

    a = [2, 7, 11, 15]
    sf = SolutionFaster()
    print(sf.twoSum(a, 9))
