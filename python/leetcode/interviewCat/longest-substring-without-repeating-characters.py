class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {} # char: index
        l = 0
        longest = 0

        for r in range(len(s)):
            char = s[r]

            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            else:
                longest = max(longest, r - l + 1)
            
            seen[char] = r
        return longest