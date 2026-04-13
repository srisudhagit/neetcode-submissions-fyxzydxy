# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = head
        newPrev = None

        while newHead != None:
            temp = newHead.next
            newHead.next = newPrev
            newPrev = newHead
            newHead = temp

        return newPrev
        