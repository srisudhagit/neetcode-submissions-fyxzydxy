/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> resList = new ArrayList<>();
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while(!queue.isEmpty()){
            int len = queue.size();
            TreeNode rightnode = null;

            for(int i=0;i<len;i++){
                TreeNode node = queue.poll();
                if(node != null){
                    rightnode = node;
                    queue.offer(rightnode.left);
                    queue.offer(rightnode.right);
                }
            }
            if(rightnode != null){
                resList.add(rightnode.val);
            }
        }
        return resList;
    }
}
