# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def gcd(self, a, b):
        remain = 1
        if a > b:
            while remain != 0:
                remain = a % b
                a = b
                b = remain
            return a
        else:
            while remain != 0:
                remain = b % a
                b = a
                a = remain
            return b

    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        next = curr.next

        while curr and next:
            gcd = self.gcd(curr.val, next.val)
            gcd_node = ListNode(gcd)
            curr.next = gcd_node
            gcd_node.next = next
            curr = curr.next.next
            next = next.next
        return head
