class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newliststart = newlistend = None

        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                if newliststart == None:
                    newliststart = newlistend = list1
                else:
                    newlistend.next = list1
                    newlistend = newlistend.next
                list1 = list1.next
            else:
                if newliststart == None:
                    newliststart = newlistend = list2
                else:
                    newlistend.next = list2
                    newlistend = newlistend.next
                list2 = list2.next

        if newliststart == None:
            return list1 if list1 else list2
        
        newlistend.next = list1 if list1 else list2
        return newliststart