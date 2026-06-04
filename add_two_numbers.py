# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0) # Dummy node helps simplify edge cases (like empty result list)
        curr = dummy   # pointer to build the result list
        carry = 0  # carry value for sums > 9
        while l1 or l2 or carry: # Loop until both lists are fully traversed AND no carry left
            # Get current values (if node exists, else 0)
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = x + y + carry # Calculate total sum of digits + carry
            carry = total // 10 # Update carry
            curr.next = ListNode(total % 10) # Create new node with last digit of total
            curr = curr.next  # Move current pointer forward
            # Move l1 and l2 forward if possible
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
