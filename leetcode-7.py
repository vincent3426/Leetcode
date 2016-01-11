#!/usr/bin/ python
# -*- coding = utf-8 -*-

__author__ = 'Sanchez Vincent'
__email__  = 'vincent3426@bupt.edu.cn'
__date__ = '2016-01-10'

class Solution(object):
    # 60ms
    def reverse(self, x):
        num = int(str(abs(x))[::-1])
        # 32-bit integer
        if num >= pow(2,31) or num < -pow(2,31):
            return 0
        if x >= 0:
            return num
        else:
            return -num

tmp = Solution()
print(tmp.reverse(2147483647))



