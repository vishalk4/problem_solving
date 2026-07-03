# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
class Solution:
    def middleNode(self, head):
        slow = head # slow moves one step at a time
        fast = head # fast moves two steps at a time
        # continue until fast reaches the end of the list
        while fast is not None and fast.next is not None:
            slow = slow.next # move slow pointer by one node
            fast = fast.next.next # move fast pointer by two nodes
        # When the loop ends:
        #   slow points to the second middle node.
        return slow
        
