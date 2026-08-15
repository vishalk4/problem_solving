# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node.
        dummy = ListNode(0)
        # current points to the last node of merged list.
        current = dummy
        while list1 and list2:
            # compare the current nodes of both lists.
            if list1.val <= list2.val:
                current.next = list1
                # move list1 to its next node.
                list1 = list1.next
            else:
                current.next = list2
                # Move list2 to its next node.
                list2 = list2.next
            # Move current to the node latest node added.
            current = current.next
        # At this point one list is empty.
        # Attach the remaining part of the other list.
        if list1:
            current.next = list1
        else:
            current.next = list2
        # return the first actual node of the merged list.
        return dummy.next
