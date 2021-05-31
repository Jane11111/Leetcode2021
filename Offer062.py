# -*- coding: utf-8 -*-
# @Time    : 2021-05-31 16:46
# @Author  : zxl
# @FileName: Offer062.py



class Solution:

    def recSolve(self,n,m):
        if n == 1:
            return 0

        idx = self.recSolve(n-1,m)

        left_idx = (m+idx)%n
        return left_idx

    def lastRemaining(self, n: int, m: int) -> int:

        ans = self.recSolve(n,m)
        return ans




