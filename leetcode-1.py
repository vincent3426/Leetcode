#!/usr/bin/ python
# -*- coding = utf-8 -*-

__author__ = 'Sanchez Vincent'
__email__  = 'vincent3426@bupt.edu.cn'
__date__ = '2016-01-10'

class Solution(object):
    # 4488ms
    # def twoSum(self, nums, target):
    #     numsCopy = list(nums)
    #     for i,value1 in enumerate(nums):
    #         numsCopy.pop(0)
    #         for j,value2 in enumerate(numsCopy):
    #             if target == (value1 + value2):
    #                 return [i + 1, i + j + 2]

    # 5920ms
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target == nums[i] + nums[j]:
                    return [i+1, j+1]

tmp = Solution()
print(tmp.twoSum([0, 4, 3, 0], 0))



