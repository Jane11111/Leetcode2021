# -*- coding: utf-8 -*-
# @Time    : 2021-03-25 16:46
# @Author  : zxl
# @FileName: 052.py


class Solution(object):


    def isOk(self,row_dic,col_dic,dia_dic1,dia_dic2,i,j):

        return not row_dic[i] and not col_dic[j] and not dia_dic1[i-j] and not dia_dic2[i+j]

    def recursiveSolve(self,row_dic,col_dic,dia_dic1,dia_dic2,i,n):
        if i>=n:
            return 1

        ans = 0

        for j in range(n):
            if self.isOk(row_dic,col_dic,dia_dic1,dia_dic2,i,j):
                row_dic[i] = True
                col_dic[j] = True
                dia_dic1[i-j] = True
                dia_dic2[i+j] = True
                ans += self.recursiveSolve(row_dic,col_dic,dia_dic1,dia_dic2,i+1,n)
                row_dic[i] = False
                col_dic[j] = False
                dia_dic1[i - j] = False
                dia_dic2[i + j] = False
        return ans

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        row_dic = {i:False for i in range(n)}
        col_dic = {i:False for i in range(n)}
        dia_dic1 = {i:False for i in range(-n,n)}
        dia_dic2 = {i: False for i in range(2*n)}

        ans = self.recursiveSolve(row_dic,col_dic,dia_dic1,dia_dic2,0,n)
        return ans



obj = Solution()
n = 1
ans = obj.totalNQueens(n)
print(ans)