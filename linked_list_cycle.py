# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head   # moves one step at a time
        fast = head   # moves two steps at a time
        while fast is not None and fast.next is not None: # we continue until fast pointer reaches end
            slow = slow.next # move slow pointer by 1 step
            fast = fast.next.next # move fast pointer by 2 steps
            if slow == fast: # check if both pointers meet 
                return True   # # if they meet cycle exists
        return False
