from typing import List
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         seen = {} # store char: index
#         left_pointer = 0
#         length = 0

#         for right_pointer in range(len(s)):
#             char = s[right_pointer]

#             if char in seen and seen[char] >= left_pointer:
#                 left_pointer = right_pointer + 1
#             else:
#                 length = max(length, right_pointer - left_pointer + 1)
#             seen[char] = right_pointer

#         return length

# solution = Solution()
# print(solution.lengthOfLongestSubstring('dsfffadfdsdfihdsfihsdhfs'))
class Solution:
    def fizzBuzz(self, n):
        arr = []
        for i in range(1, n+1):
            s = ''

            if i % 3 == 0:
                s += 'Fizz'
            if i % 5 == 0:
                s += 'Buzz'
            
            if not s:
                s = str(n)
            arr.append(s)
        return arr

sol = Solution()
print(sol.fizzBuzz(3))