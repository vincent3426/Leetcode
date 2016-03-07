class Solution(object):
    # 196ms 4.59%
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        char = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        char = {value:key for key,value in char.items()}
        res = ''
        coe = []
        order = sorted(list(char.keys()), reverse=True)
        for value in order:
            coe.append(int(num/value))
            num -= int(num/value)*value
        i = 0
        while i < len(coe):
            if i == 6:
                str = coe[i]*char.get(order[i])
            elif i == 1 and coe[i+1] == 4:
                if coe[i] == 0 :
                    str = 'CD'
                else: 
                    str = 'CM'
                i += 1
            elif i == 3 and coe[i+1] == 4:
                if coe[i] == 0 :
                    str = 'XL'
                else:
                    str = 'XC'
                i += 1
            elif i == 5 and coe[i+1] == 4:
                if coe[i] == 0 :
                    str = 'IV'
                else:
                    str = 'IX'
                i += 1
            else:
                str = coe[i]*char.get(order[i])
            res += str
            i += 1
        return res
