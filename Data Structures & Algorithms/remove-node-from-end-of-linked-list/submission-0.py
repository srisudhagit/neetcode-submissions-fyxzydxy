# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        listlen = 0
        temp = head

        while temp:
            listlen += 1
            temp = temp.next
        
        i = 0
        temp = head
        prev = None
        while i < listlen-n:
            i += 1
            prev = temp
            temp = temp.next

        if prev == None:
            return head.next
        else:
             prev.next = temp.next
             return head

