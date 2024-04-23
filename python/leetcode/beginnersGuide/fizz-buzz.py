"""
https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4424/

Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

"""

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        # Note: start from 1
        arr = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                arr.append('FizzBuzz')
            elif i % 3 == 0:
                arr.append('Fizz')
            elif i % 5 == 0:
                arr.append('Buzz')
            else:
                arr.append(str(i))

        return arr
    
        # string concatination (easy to extend)
        # arr = []
        # for i in range(1, n+1):
        #     curStr = ''

        #     if i % 3 == 0:
        #         curStr += 'Fizz'
        #     if i % 5 == 0:
        #         curStr += 'Buzz'
        #     if not curStr:
        #         curStr = str(i)

        #     arr.append(curStr)

        # return arr