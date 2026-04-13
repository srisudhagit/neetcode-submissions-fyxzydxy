# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head
        #find the middle of the linkedlist
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #split into 2 halves and reverse second list
        secondList = slow.next
        prev = slow.next = None
        while secondList:
            temp = secondList.next
            secondList.next = prev
            prev = secondList
            secondList = temp

        #merge the 2 linkedlists
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

