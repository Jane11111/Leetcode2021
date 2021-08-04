# -*- coding: utf-8 -*-
# @Time    : 2021-08-04 13:38
# @Author  : zxl
# @FileName: 089_2.py


class Solution:
    def grayCode(self, n: int) :


        if n == 0:
            return [0]
        if n == 1:
            return [0,1]

        ans = [0,1]
        for i in range(2,n+1):

            n = len(ans)

            for j in range(n):
                ans[j] *=2

            for j in range(n-1,-1,-1):
                ans.append(ans[j]+1)
        return ans

