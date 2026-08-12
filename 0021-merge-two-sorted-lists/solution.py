# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        p1 = list1
        p2 = list2
        tail = dummy
        while p1 and p2:
            if p1.val <= p2.val:
                tail.next = p1
                tail = tail.next
                p1 = p1.next
            else:
                tail.next = p2
                tail = tail.next
                p2 = p2.next
        tail.next = p1 if p1 else p2
        return dummy.next
