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
    // 4ms 0.69%
    // Recursive
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> tmp, ret;
        if(!root) return ret;
        tmp = postorderTraversal(root->left);
        ret.insert(ret.end(), tmp.begin(), tmp.end());
        tmp = postorderTraversal(root->right);
        ret.insert(ret.end(), tmp.begin(), tmp.end());
        ret.push_back(root->val);
        return ret;
    }
};
