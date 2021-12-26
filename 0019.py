# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = 0
        cur = head
        while cur != None:
            length += 1
            cur = cur.next
        if length >1:
            cur = head
            prev = None
            for i in range(length-n):
                prev = cur
                cur = cur.next
            if prev != None:
                prev.next = cur.next
            else:
                head = cur.next
            return head
        else:
            return None