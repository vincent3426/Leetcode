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
    // 0ms 12.54%
    // Recursive
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> tmp, ret;
        if(!root) return ret;
        tmp = inorderTraversal(root->left);
        ret.insert(ret.end(), tmp.begin(), tmp.end());
        ret.push_back(root->val);
        tmp = inorderTraversal(root->right);
        ret.insert(ret.end(), tmp.begin(), tmp.end());
        return ret;
    }
};
