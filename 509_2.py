# -*- coding: utf-8 -*-
# @Time    : 2021-05-16 16:20
# @Author  : zxl
# @FileName: 509_2.py



class Solution:

    def mymulti(self,a,b):
        ans = [[0,0],[0,0]]
        for i in range(2):
            for j in range(2):
                ans[i][j] = a[i][0]*b[0][j]+a[i][1]*b[1][j]
        return ans

    def mypow(self,mat,n):

        res = [[1,0],[0,1]]
        tmp = mat
        while n>0:
            if n%2:
                res = self.mymulti(res,tmp)
            n>>=1
            tmp = self.mymulti(tmp,tmp)
        return res


    def fib(self, n: int) -> int:
        if n<2:
            return n

        mat = [[1,1],[1,0]]
        new_mat = self.mypow(mat,n-1)
        return new_mat[0][0]
