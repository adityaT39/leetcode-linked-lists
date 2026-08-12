# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def reverse_list(self, head):
        before = None
        temp = head
        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return before

    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        reverse_head = self.reverse_list(head)
        curr = reverse_head
        prev = None
        max_so_far = 0

        while curr:
            if curr.val < max_so_far:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
                max_so_far = prev.val

        original_head = self.reverse_list(reverse_head)
        return original_head
