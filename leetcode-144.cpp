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
    // 4ms 0.06%
    // Recursive
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> tmp, ret;
        if(!root) return ret;
        ret.push_back(root->val);
        tmp = preorderTraversal(root->left);
        ret.insert(ret.end(), tmp.begin(), tmp.end());
        tmp = preorderTraversal(root->right);
        ret.insert(ret.end(), tmp.begin(), tmp.end());
        return ret;
    }
};
