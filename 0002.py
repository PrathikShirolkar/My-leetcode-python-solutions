# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        one_str = ""
        while l1 != None:
            one_str += str(l1.val)
            l1 = l1.next 
        one = int(one_str[::-1])
        
        two_str = ""
        while l2 != None:
            two_str += str(l2.val)
            l2 = l2.next 
        two = int(two_str[::-1])
        
        final = str(one+two)[::-1]
        fin =ListNode(final[0])
        head = fin
        for i in final[1:]:
            fin.next = ListNode(i)
            fin = fin.next
        return head
        