# -*- coding: utf-8 -*-
# @Time    : 2021-08-04 14:58
# @Author  : zxl
# @FileName: 091_2.py




class Solution:

    def recFind(self,s,dic):

        if s in dic:
            return dic[s]
        if len(s) ==0:
            return 1
        if len(s) == 1:
            return int(s!='0')
        if s[0] == '0':
            return 0

        n1 = self.numDecodings(s[1:])
        if s[0]!='0' and s[:2]<='26':
            n2 = self.numDecodings(s[2:])
        else:
            n2 = 0
        dic[s] = n1+n2
        return n1+n2


    def numDecodings(self, s: str) -> int:

        ans = self.recFind(s,{})
        return ans


