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
    public TreeNode invertTree(TreeNode root) {
        TreeNode temp,left, right;
        if(root == null || isLeaf(root)){
            return root;
        }
        left = root.left;
        right = root.right;
        TreeNode invertLeft = invertTree(left);
        TreeNode invertRight = invertTree(right);
        root.left = invertRight;
        root.right = invertLeft;
        return root;
    }

    public boolean isLeaf(TreeNode node){
        return node.left == null && node.right == null;
    }
}
