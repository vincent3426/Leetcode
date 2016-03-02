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
    int maxDepth(TreeNode* root) {
        int n;
        if(root == NULL)
            n = 0;
        else{
            n = max(maxDepth(root->left)+1, maxDepth(root->right)+1);
        }
    }
};
