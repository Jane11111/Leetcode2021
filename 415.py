# -*- coding: utf-8 -*-
# @Time    : 2021-05-15 11:45
# @Author  : zxl
# @FileName: 415.py




class Solution:
    def addStrings(self, num1: str, num2: str) -> str:


        base = 0
        i = len(num1)-1
        j = len(num2)-1
        ans = ''
        while i>=0 or j>=0:
            if i<0:
                n1 = 0
            else:
                n1 = int(num1[i])

            if j<0:
                n2 = 0
            else:
                n2 = int(num2[j])
            v = n1+n2+base

            base = v//10
            v = v%10
            ans = str(v)+ans
            i-=1
            j-=1
        if base:
            ans = str(base)+ans
        return ans

