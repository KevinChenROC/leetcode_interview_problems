# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # edge cases
        if not l1 and l2:
            return l2
        elif not l2 and l1:
            return l1
        elif not l2 and not l1:
            return l1

        sorted_li = None
        if l1.val <= l2.val:
            sorted_li = l1
            l1 = l1.next
        else:
            sorted_li = l2
            l2 = l2.next

        head = sorted_li
        while l1 and l2:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next

            head = head.next

        if not (l1) and l2:
            head.next = l2
        elif not (l2) and l1:
            head.next = l1

        return sorted_li
