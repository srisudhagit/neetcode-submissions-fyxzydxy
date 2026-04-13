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
    public boolean hasCycle(ListNode head) {
        Map<ListNode,ListNode> nextnodes = new HashMap<>();
        ListNode temp = head;
        while(temp != null){
            if(!nextnodes.containsKey(temp)){
                nextnodes.put(temp,temp.next);
            }else{
                return true;
            }
            temp = temp.next;
        }
       return false;
    }
}
