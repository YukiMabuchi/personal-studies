"""
https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4427/

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
       
        # time complexity = O(m)
        # space complexity = O(k) // k == number of letters in magazine, 26 at most in this prob, so O(1)
        availableChars = {} # char: count

        for i in range(len(magazine)):
            char = magazine[i]
            currentCount = availableChars.get(char, 0)
            availableChars[char] = currentCount + 1

        for j in range(len(ransomNote)):
            char = ransomNote[j]
            currentCount = availableChars.get(char, 0)
            if currentCount == 0:
                return False
            
            availableChars[char] = currentCount - 1
        
        return True
    
        #簡略化version
        # seen = {} # char: count

        # for _, letter in enumerate(magazine):
        #     count = seen.get(letter, 0)
        #     seen[letter] = count+1
        
        # for _, s in enumerate(ransomNote):
        #     count = seen.get(s, 0)
        #     if count == 0:
        #         return False
            
        #     seen[s] -= 1
        
        # return True