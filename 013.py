# -*- coding: utf-8 -*-
# @Time    : 2021-03-02 10:11
# @Author  : zxl
# @FileName: 013.py

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic1 = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        dic2 = {'IV':4, 'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}

        res = 0
        i = 0
        while i <= len(s) - 1:
            if i == len(s)-1:
                res += dic1[s[i]]
                i+=1
            else:
                if s[i:i+2] in dic2:
                    res += dic2[s[i:i+2]]
                    i+=2
                else:
                    res += dic1[s[i]]
                    i+=1



        return res


obj = Solution()
s = 'MCMXCIV'
res = obj.romanToInt(s)
print(res)

