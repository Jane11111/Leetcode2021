# -*- coding: utf-8 -*-
# @Time    : 2021-04-02 09:57
# @Author  : zxl
# @FileName: 861.py


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
        for i in range(m):
            if A[i][0] == 0:
                for j in range(n):
                    A[i][j] = 1-A[i][j]
        ans = 0
        for i in range(n-1,-1,-1):
            base = 2**(n-1-i)
            c1 =sum(A[:,i])
            c2 = m-c1
            ans += max(c1,c2)*base
        return ans

obj = Solution()
A = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
ans = obj.matrixScore(A)
print(ans)


