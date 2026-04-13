/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev,first, second,temp;
        if(head == null){
            return null;
        }
        prev = null;
        first = head;
        second=head.next;
        while(second!=null){
            temp = second.next;
            second.next = first;
            first.next = prev;
            if(temp == null){
                return second;
            }else{
                prev = first;
                first = second;
                second = temp;
            }
        }
        return head;
    }
}
