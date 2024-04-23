"""
https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4425/

Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

 

Example 1:

Input: num = 14
Output: 6
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.

"""


class Solution:
    def numberOfSteps(self, num: int) -> int:

        # original
        # time complexity = O(logn)
        # space complexity = O(1)
        # steps = 0
        # while num > 0:
        #     if num % 2 == 0:
        #         num /= 2
        #     else:
        #         num -= 1
        #     steps += 1

        # return steps
    
        #Bitwise approach
        # time complexity = O(logn)
        # space complexity = O(1)
        """
        Binary representation of integers
        Bitwise Shift Operators
        Bitwise Logical Operators
        Bitmasks
        """

        steps = 0
        while num > 0:
            if num & 1 == 0: # use bitmask to check if num is even
                num >>= 1
            else:
                num -= 1
            steps += 1

        return steps
    
sol = Solution()
print(sol.numberOfSteps(32))

