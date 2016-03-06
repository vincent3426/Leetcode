class Solution(object):
    # 164ms
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        tmp = []
        cnt = 0
        flag = 0
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                res_tmp = nums[i] + nums[j] + nums[k] - target
                cnt += 1
                if cnt == 1:
                    res = abs(res_tmp)
                    tmpNum = nums[i] + nums[j] + nums[k]
                elif abs(res_tmp) < res:
                    flag = 1
                    res = abs(res_tmp)
                    tmp.append(nums[i] + nums[j] + nums[k])
                if res_tmp == 0:
                    return target
                elif res_tmp < 0:
                    j += 1
                else:
                    k -= 1
        if flag == 1:
            return tmp[-1]
        else:
            return tmpNum
