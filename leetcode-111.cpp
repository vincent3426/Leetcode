/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    // 12ms 6.37%
    int minDepth(TreeNode* root) {
        if(!root) return 0;
        if(!root->left && !root->right) return 1;
        if(!root->left) return minDepth(root->right)+1;
        else if(!root->right) return minDepth(root->left)+1;
        else return min(minDepth(root->left)+1, minDepth(root->right)+1);
    }
};
