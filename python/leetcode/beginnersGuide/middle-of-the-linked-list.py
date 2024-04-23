"""
https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4426/

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

"""

# Linked list is a chain of nodes

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head):

        # first approach
        # time complexity = O(n)
        # space complexity = O(n)
        # using a copy of an array defeats good points of using linked list
        # array = []

        # while head is not None:
        #     array.append(head) # linked list has only a reference of its first element
        #     head = head.next

        # return array[len(array) // 2]
    
        # second approach, utilizing linked list
        # time complexity = O(n)
        # space complexity = O(1)
        middle = end = head

        while end and end.next:
            middle = middle.next
            end = end.next.next
        
        return middle
