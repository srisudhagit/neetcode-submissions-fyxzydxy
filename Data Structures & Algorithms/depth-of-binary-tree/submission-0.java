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
    public int maxDepth(TreeNode root) {
        if(root == null){
            return 0;
        }else if(isLeaf(root)){
            return 1;
        }else{
            int leftdepth = maxDepth(root.left);
            int rightdepth = maxDepth(root.right);
            return 1+max(leftdepth,rightdepth);
        }
    }

    int max(int a,int b){
        return ((a >= b) ? a : b);
    }

    boolean isLeaf(TreeNode node){
        return (node.left == null && node.right == null);
    }
}
