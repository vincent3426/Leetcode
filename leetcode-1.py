#!/usr/bin/ python
# -*- coding = utf-8 -*-

__author__ = 'Sanchez Vincent'
__email__  = 'vincent3426@bupt.edu.cn'
__date__ = '2016-01-10'

class Solution(object):
    # 4488ms
    # O(N^2)
    # def twoSum(self, nums, target):
    #     numsCopy = list(nums)
    #     for i,value1 in enumerate(nums):
    #         numsCopy.pop(0)
    #         for j,value2 in enumerate(numsCopy):
    #             if target == (value1 + value2):
    #                 return [i + 1, i + j + 2]

    # 5920ms
    # def twoSum(self, nums, target):
    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if target == nums[i] + nums[j]:
    #                 return [i+1, j+1]
    
    # UPDATE (2016/2/13):
    # The return format had been changed to zero-based indices. Please read the above updated description carefully.
    # 44ms
    # O(NlogN)
    def twoSum(self, nums, target):
        nums_tmp = sorted(nums)
        i = 0
        j = len(nums)-1
        while(i < j):
            if(nums_tmp[i] + nums_tmp[j] == target):
                if nums_tmp[i] != nums_tmp[j]:
                    res = [nums.index(nums_tmp[i]), nums.index(nums_tmp[j])]
                    res.sort()
                    return res
                else:
                    res = [m for m, k in enumerate(nums) if k == nums_tmp[i]]
                    return res
            elif nums_tmp[i] + nums_tmp[j] < target:
                i += 1
            else:
                j -= 1

tmp = Solution()
print(tmp.twoSum([0, 4, 3, 0], 0))



