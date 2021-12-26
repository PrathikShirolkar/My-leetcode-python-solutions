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
        print(l1)
        print(l2)
        
        if l1!=None or l2!=None:
            one = l1
            two = l2
            sort = []
            while one!=None or two!=None:
                if one!=None and two!=None:
                    print("if")
                    if one.val > two.val:
                        sort.append(two.val)
                        two = two.next
                    else:
                        sort.append(one.val)
                        one = one.next
                else:
                    print("else")
                    if one==None:
                        while two!=None:
                            sort.append(two.val)
                            two = two.next
                    else:
                        while one!=None:
                            sort.append(one.val)
                            one = one.next
            head = ListNode()
            cur = head
            prev = None
            for i in sort:
                cur.val = i
                cur.next = ListNode()
                prev = cur
                cur = cur.next
            prev.next=None
            return head
        else:
            return None
        