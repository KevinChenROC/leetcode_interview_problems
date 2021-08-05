# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        reverse_head = None
        while head:
            next_node = head.next
            head.next = reverse_head
            reverse_head = head
            head = next_node

        return reverse_head
