# -*- coding: utf-8 -*-
# @Time    : 2021-03-02 09:50
# @Author  : zxl
# @FileName: 007.py

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        s = str(x)
        neg = False
        if s[0] == '-':
            neg = True
            s = s[1:]
        res = ''
        for i in range(len(s)-1, -1,-1):
            res += s[i]
        i = 0
        while res[i] == '0' and i < len(res)-1:
            i+=1
        res = res[i:]
        if neg:
            res = '-' + res
        if float(res) < -2**31 or float(res) > 2**31 - 1:
            return 0
        else:
            return int(res)


obj = Solution()

x = 1563847412
print(int(x))

res = obj.reverse(x)
print(res)