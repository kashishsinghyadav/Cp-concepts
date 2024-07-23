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

         
       
    public int maxLevelSum(TreeNode root) {
        if (root == null) return 0;

        Queue<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        int maxSum = Integer.MIN_VALUE;
        int maxLevel = 1;
        int currentLevel = 1;

        while (!q.isEmpty()) {
            int levelSize = q.size();
            int currentSum = 0;

            for (int i = 0; i < levelSize; i++) {
                TreeNode node = q.poll();
                currentSum += node.val;

                if (node.left != null) q.add(node.left);
                if (node.right != null) q.add(node.right);
            }

            if (currentSum > maxSum) {
                maxSum = currentSum;
                maxLevel = currentLevel;
            }

            currentLevel++;
        }

        return maxLevel;

        
    }
}
