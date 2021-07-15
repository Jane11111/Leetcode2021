# -*- coding: utf-8 -*-
# @Time    : 2021-07-12 15:42
# @Author  : zxl
# @FileName: 037_1.py



class Solution:


    def getNext(self,i,j,m,n):

        if j+1<n:
            return i,j+1
        return i+1,0


    def recSolve(self,board,i,j,m,n,row_dic,col_dic,box_dic):

        if i>=m or j>=n:
            return True

        box_num = 3*(i//3)+j//3
        x, y = self.getNext(i, j, m, n)

        if board[i][j] !='.':
            return self.recSolve(board,x,y,m,n,row_dic,col_dic,box_dic)

        for k in range(1,10):

            s = str(k)

            if (s not in row_dic[i] or not row_dic[i][s]) and\
                (s not in col_dic[j] or not col_dic[j][s]) and \
                (s not in box_dic[box_num] or not box_dic[box_num][s]):
                row_dic[i][s] = True
                col_dic[j][s] = True
                box_dic[box_num][s] = True
                board[i][j] = s

                f = self.recSolve(board,x,y,m,n,row_dic,col_dic,box_dic)
                if f:
                    return True
                row_dic[i][s] = False
                col_dic[j][s] = False
                box_dic[box_num][s] = False
                board[i][j] = '.'
        return False







    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        row_dic = {i:{} for i in range(9)}
        col_dic = {i:{} for i in range(9)}
        box_dic = {i:{} for i in range(9)}


        for i in range(9):
            for j in range(9):
                box_num = 3*(i//3)+j//3
                if board[i][j]!='.':
                    s = board[i][j]
                    row_dic[i][s] = True
                    col_dic[j][s] = True
                    box_dic[box_num][s] = True
        m = len(board)
        n = len(board[0])
        self.recSolve(board,0,0,m,n,row_dic,col_dic,box_dic)



