class Solution:
    def twoSum(self, nums, target):
        seen = {} # n: index

        for i, n in enumerate(nums):
            remaining = target - n
            if remaining in seen:
                return [seen[remaining], i]

            seen[n] = i