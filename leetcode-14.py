class Solution(object):
    # 44ms 76.31%
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0 :
            return "" 
        length = [len(str) for str in strs]
        if 0 in length:
            return ""
        res = ''
        tmp = [[str[i] for str in strs] for i in range(min(length))]
        cnt = 0
        while cnt < len(tmp) and tmp[cnt].count(tmp[cnt][0]) == len(strs):
            res += tmp[cnt][0]
            cnt += 1
        return res
