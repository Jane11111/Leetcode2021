# -*- coding: utf-8 -*-
# @Time    : 2021-04-02 10:05
# @Author  : zxl
# @FileName: 861_2.py

class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        import numpy as np
        A = np.array(A)

        m = len(A)
        n = len(A[0])

        c1 = A[:,0]
        ans = 2**(n-1) *m
        for j in range(1,n):
            c2 = A[:,j]
            c2 = 1-c1^c2

            ans += max(sum(c2),m-sum(c2)) * (2**(n-1-j))
        return ans

obj = Solution()
A = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
ans = obj.matrixScore(A)
print(ans)

