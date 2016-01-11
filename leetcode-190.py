#!/usr/bin/ python
# -*- coding = utf-8 -*-

__author__ = 'Sanchez Vincent'
__email__  = 'vincent3426@bupt.edu.cn'
__date__ = '2016-01-10'

class Solution(object):
    def reverseBits(self, n):
        # 52ms
        # 32-bits unsigned integer
        tmpBits = bin(n)[2:]
        prefix = ''.join(['0']*(32-len(tmpBits)))
        return int((prefix+tmpBits)[::-1], 2)

tmp = Solution()
print(tmp.reverseBits(1))