# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        num_set = set(nums)  # convert list to set so that we can get a time complexity of O(1)
        cnt = 0            # to count connected components
        c = head       # start from head of linked list
        while c:
            if c.val in num_set: # Check if c node is part of nums
                # if next node is None OR not in nums it means this is the end of a component
                if c.next is None or c.next.val not in num_set:
                    cnt += 1  # found one complete component
            c = c.next # Move to next node
        return cnt
