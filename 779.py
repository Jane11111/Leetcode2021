# -*- coding: utf-8 -*-
# @Time    : 2021-03-06 15:54
# @Author  : zxl
# @FileName: 779.py

# TODO 参考别人答案

class Solution(object):

    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N == 1 and K == 1:
            return 0
        a = self.kthGrammar(N-1,int((K+1)/2))
        if K % 2:
            return a
        else:
            return 1-a

obj = Solution()
N = 3
K = 2
res = obj.kthGrammar(N,K)
print(res)
