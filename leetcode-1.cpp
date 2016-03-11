class Solution {
public:
    # 30ms 27.64%
    vector<int> twoSum(vector<int> &numbers, int target) {
        vector<int> ret(2, -1);
	map<int, int> m;    //value->index map
	for (unsigned int i = 0; i < numbers.size(); i++) {
	    m[numbers[i]] = i;
	}
	for (unsigned int i = 0; i < numbers.size(); i++) {
	    int tmp = target - numbers[i];
	    if (m.find(tmp) != m.end() && m[tmp] != (int)i){
		ret[0] = i;
		ret[1] = m[tmp];
		break;
	    }
	}
	return ret;
    }
};
