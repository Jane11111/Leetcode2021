# -*- coding: utf-8 -*-
# @Time    : 2021-06-01 09:42
# @Author  : zxl
# @FileName: 008_2.py



class Solution:
    def myAtoi(self, s: str) -> int:


        sub_s = ''

        i = 0
        while i<len(s) and s[i] == ' ':
            i+=1

        neg_op = False
        if i<len(s):
            if s[i] == '-':
                neg_op = True
                i+=1
            elif s[i] == '+':
                neg_op = False
                i+=1
            while i<len(s) and s[i].isnumeric():
                sub_s+=s[i]
                i+=1
        s = sub_s
        i = 0
        while i<len(s) and s[i] == '0':
            i+=1

        if i>=len(s):
            return 0
        s = s[i:]
        if neg_op:
            if len(s)>10 or float(s)> 2.0**31:
                s = -2.0**31
            else:
                s = -int(s)
        else:
            if len(s) >10 or float(s)>2.0**31-1:
                s = 2.0**31-1
            else:
                s = int(s)
        return int(s)


obj = Solution()
s = '-91283472332'
ans = obj.myAtoi(s)
print(ans)
