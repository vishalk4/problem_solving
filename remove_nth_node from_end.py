# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        # initialize two pointers
        fast = dummy
        slow = dummy
        # move fast pointer n+1 steps ahead
        # so that gap between fast and slow is n
        for _ in range(n + 1):
            fast = fast.next
        # move both pointers until fast reaches end
        while fast:
            fast = fast.next
            slow = slow.next
        # remove the nth node from end
        # slow is just before the node to delete
        slow.next = slow.next.next
        # return new head
        return dummy.next
