# -*- coding: utf-8 -*-
# @Time    : 2021-03-25 16:08
# @Author  : zxl
# @FileName: 051.py


class Solution(object):

    def isOk(self,row_dic,col_dic,dia_dic1,dia_dic2,i,j):
        return not row_dic[i] and not col_dic[j] and not dia_dic1[i-j] and not dia_dic2[i+j]



    def recursiveSolve(self,row_dic,col_dic,dia_dic1,dia_dic2,i,matrix):

        n = len(matrix)
        if i>=n:
            new_matrix = []
            for i in range(len(matrix)):
                arr = []
                for j in range(len(matrix[0])):
                    arr.append(matrix[i][j])
                new_matrix.append(arr)
            return [new_matrix]



        ans = []


        for j in range(0,n):
            if self.isOk(row_dic,col_dic,dia_dic1,dia_dic2,i,j):


                matrix[i][j] = 'Q'
                row_dic[i] = True
                col_dic[j] = True
                dia_dic1[i-j] = True
                dia_dic2[i+j] = True
                sub_ans = self.recursiveSolve(row_dic,col_dic,dia_dic1,dia_dic2,i+1,matrix)
                if len(sub_ans) != 0:
                    ans.extend(sub_ans)

                matrix[i][j] = '.'
                row_dic[i] = False
                col_dic[j] = False
                dia_dic1[i - j] = False
                dia_dic2[i + j] = False


        return ans



    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        row_dic = {i:False for i in range(n)}
        col_dic = {i:False for i in range(n)}
        dia_dic1 = {i:False for i in range(-(n),n)}
        dia_dic2 = {i: False for i in range(2*(n)+1)}

        matrix = []
        for i in range(n):
            arr = []
            for j in range(n):
                arr.append('.')
            matrix.append(arr)
        matrix_ans = self.recursiveSolve(row_dic,col_dic,dia_dic1,dia_dic2,0,matrix)
        ans = []
        for matrix in matrix_ans:
            str_matrix = []
            for row in matrix:
                str_matrix.append(''.join(row))
            ans.append(str_matrix)



        return ans

obj = Solution()
n = 4
ans = obj.solveNQueens(n)
print(ans)


