class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        vector<int> tmp=nums;
    	for(unsigned int i=0; i<nums.size(); i++){
    		tmp[i]=nums[(i+nums.size()-k%nums.size())%nums.size()];
    	}
    	nums=tmp;
    }
};
