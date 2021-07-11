# -*- coding: utf-8 -*-
# @Time    : 2021-07-07 11:52
# @Author  : zxl
# @FileName: 013_2.py



class Solution:
    def romanToInt(self, s: str) -> int:
        # dic = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M',
        #        4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,
               'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}


        ans = 0

        i = 0
        while i<len(s):

            if i+1<len(s) and s[i:i+2] in dic:
                ans += dic[s[i:i+2]]
                i+=2
            else:
                ans += dic[s[i:i+1]]
                i+=1
        return ans






