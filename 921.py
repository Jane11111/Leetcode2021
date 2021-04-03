# -*- coding: utf-8 -*-
# @Time    : 2021-04-02 15:58
# @Author  : zxl
# @FileName: 921.py

class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """

        lst = []
        for s in S:

            if not lst or lst[-1] == s or (lst[-1] == ')' and s =='('):
                lst.append(s)
            else:
                lst.pop(-1)
        return len(lst)

obj = Solution()
S = "()))(("
ans = obj.minAddToMakeValid(S)
print(ans)