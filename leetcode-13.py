
class Solution(object):
    # 184ms
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        char = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = char.get(s[0])
        for i in range(1, len(s)):
            if char.get(s[i]) > char.get(s[i-1]):
                res += char.get(s[i])-2*char.get(s[i-1])
            else:
                res += char.get(s[i])
        return res
