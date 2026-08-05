# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while prev.next and prev.next.next:
            # nodes to swap
            first = prev.next
            second = prev.next.next
            # swapping
            prev.next = second
            first.next = second.next
            second.next = first
            # move prev to next pair
            prev = first
        return dummy.next
