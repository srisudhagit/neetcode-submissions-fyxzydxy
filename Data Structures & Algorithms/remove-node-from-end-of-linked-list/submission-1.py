# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        second = head
        i = 0
        while second and i < n:
            second = second.next
            i += 1
        if second == None:
            return head.next
        prev = None
        while second:
            prev = first
            first = first.next
            second = second.next

        prev.next = first.next

        return head
        