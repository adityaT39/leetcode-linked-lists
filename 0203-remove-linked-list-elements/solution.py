# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = prev.next
                curr = curr.next
        return dummy.next


# Alternate approach: curr/runner pointer style instead of prev/curr.
class SolutionRunner(object):
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        while curr:
            run = curr.next
            while run and run.val == val:
                run = run.next
            curr.next = run
            curr = curr.next
        return dummy.next
