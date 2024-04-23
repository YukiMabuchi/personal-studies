"""
https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

"""

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        sums = [nums[0]]
        for i in range(1, len(nums)):
            sums.append(sums[i-1]+nums[i])
        return sums
    
        # modify input array
        # for i in range(1, len(nums)):
        #     nums[i] += nums[i-1]
        # return nums
    

    
sol = Solution()
print(sol.runningSum([1, 2, 3, 4]))