#!/usr/bin python
# -*- coding:utf-8 -*-

__author__ = 'Sanchez Vincent'
__email__  = 'vincent3426@bupt.edu.cn'
__date__ = '2016-01-09'

class Solution(object):
    # 40ms
    def reverseWords(self, s):
        l1 = s.strip(' ').split(' ')
        l2 = []
        [l2.append(i) for i in l1 if i != '']
        return ' '.join(l2[::-1])

tmp = Solution()
print(tmp.reverseWords(' the sky    is very blue and i very   love it  '))