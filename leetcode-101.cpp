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
    // 4ms 14.2%
    bool isSymmetric(TreeNode* root) {
        if(!root) return true;
        return isSymmetric(root->left, root->right);
    }
    bool isSymmetric(TreeNode* left, TreeNode* right){
        if(!left && !right) return true;
        if((left && !right) || (right && !left) || (left->val != right->val)) return false;
        return isSymmetric(left->left, right->right) && isSymmetric(left->right, right->left);
    }
};
