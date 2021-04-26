# -*- coding: utf-8 -*-
# @Time    : 2021-04-26 22:55
# @Author  : zxl
# @FileName: 289.py



class Solution:
    def gameOfLife(self, board )  :
        """
        Do not return anything, modify board in-place instead.
        """

        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):

                count = 0
                if i-1>=0 and board[i-1][j]>=1:
                    count+=1
                if i+1<m and board[i+1][j]>=1:
                    count+=1
                if j-1>=0 and board[i][j-1]>=1:
                    count+=1
                if j+1<n and board[i][j+1]>=1:
                    count+=1
                if i-1>=0 and j-1>=0 and board[i-1][j-1]>=1:
                    count+=1
                if i+1<m and j+1<n and board[i+1][j+1]>=1:
                    count+=1
                if i+1<m and j-1>=0 and board[i+1][j-1]>=1:
                    count+=1
                if i-1>=0 and j+1<n and board[i-1][j+1]>=1:
                    count+=1

                if board[i][j] and (count<2 or count >3):
                    board[i][j]=2
                if board[i][j]==0 and count == 3:
                    board[i][j] = -1
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                if board[i][j] == -1:
                    board[i][j] = 1
