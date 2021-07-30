# -*- coding: utf-8 -*-
# @Time    : 2021-07-28 21:20
# @Author  : zxl
# @FileName: 816.py


class Solution:

    def split_colon(self,s):
        if len(s) == 1:
            return [s]
        if s[0] == '0':
            return [s[0]+'.'+s[1:]]
        if s[-1] == '0':
            return [s]
        lst = []
        for i in range(len(s)-1):
            news = s[:i+1]+'.'+s[i+1:]
            lst.append(news)
        lst.append(s)
        return lst

    def check(self,s):
        if len(s) <= 1:
            return True
        if s[0] == '0' and s[-1] == '0':
            return False
        return True


    def split_comma(self,s):

        ans = []
        for i in range(len(s)-1):

            l = s[:i+1]
            r = s[i+1:]
            if not self.check(l) or not self.check(r):
                continue
            lst1 = self.split_colon(l)
            lst2 = self.split_colon(r)
            for num1 in lst1:
                for num2 in lst2:
                    ans.append('('+num1+','+num2+')')
        return ans



    def ambiguousCoordinates(self, s: str) :

        ans = self.split_comma(s[1:-1])
        return ans

obj = Solution()
s = "(100)"
ans = obj.ambiguousCoordinates(s)
print(ans)





