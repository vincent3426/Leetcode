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
    // 8ms 5.22%
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ret;
        levelOrder(root, 0, ret);
        return ret;
    }
    void levelOrder(TreeNode* root, int level, vector<vector<int>> &ret){
        if(!root) return;
        if(ret.size() == level) ret.push_back({});
        ret[level].push_back(root->val);
        levelOrder(root->left, level+1, ret);
        levelOrder(root->right, level+1, ret);
    }
};
