# -*- coding: utf-8 -*-
# @Time    : 2021-08-03 20:18
# @Author  : zxl
# @FileName: 079_5.py



class Solution:

    def dfs(self,board,word,idx,i,j,m,n):
        if idx == len(word):
            return True

        for x,y in [[i-1,j],[i,j-1],[i,j+1],[i+1,j]]:

            if x<0 or x>=m or y<0 or y>=n:
                continue

            if board[x][y] == word[idx]:
                tmp = board[x][y]
                board[x][y] = '.' # 标记visited
                f = self.dfs(board,word,idx+1,x,y,m,n)
                board[x][y] = tmp
                if f :
                    return True
        return False




    def exist(self, board, word: str) :


        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    board[i][j] = '.'
                    f = self.dfs(board,word,1,i,j,m,n)
                    board[i][j] = word[0]
                    if f:
                        return True
        return False