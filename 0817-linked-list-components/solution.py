# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def numComponents(self, head, nums):
        """
        :type head: Optional[ListNode]
        :type nums: List[int]
        :rtype: int
        """
        curr = head
        connected_component = 0
        in_connected_component = False

        while curr:
            if curr.val in nums:
                if not in_connected_component:
                    connected_component += 1
                in_connected_component = True
            else:
                in_connected_component = False
            curr = curr.next
        return connected_component
