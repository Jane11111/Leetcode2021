# -*- coding: utf-8 -*-
# @Time    : 2021-07-14 08:56
# @Author  : zxl
# @FileName: SHIEN01.py


class Solution:

    def recurFind(self,s,dic):
        if s in dic:
            return dic[s]
        if len(s) == 0:
            return 1

        if s[0] == '0':
            dic[s] = 0
            return 0
        if len(s) == 1:
            dic[s] = 1
            return 1
        n1 = self.recurFind(s[1:],dic)
        n2 = 0
        if s[:2]>='10' and s[:2]<='26':
            n2 = self.recurFind(s[2:],dic)
        ans = n1+n2
        dic[s] = ans
        return ans



    def numDecoding(self, s):

        ans = self.recurFind(s,{})
        return ans

obj = Solution()
s = '0'
ans = obj.numDecoding(s)
print(ans)



