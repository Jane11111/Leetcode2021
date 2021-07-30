# -*- coding: utf-8 -*-
# @Time    : 2021-07-17 21:27
# @Author  : zxl
# @FileName: 079_4.py





class Solution:

    def dfs(self,board,visited,x,y,m,n,word,idx):
        if idx == len(word):
            return True

        for newx,newy in [[x+1,y],[x,y+1],[x,y-1],[x-1,y]]:
            if newx<0 or newx>=m or newy<0 or newy>=n:
                continue
            if not visited[newx][newy] and board[newx][newy] == word[idx]:
                visited[newx][newy] = True
                f = self.dfs(board,visited,newx,newy,m,n,word,idx+1)
                if f:
                    return f
                visited[newx][newy] = False




    def exist(self, board, word: str) -> bool:

        m = len(board)
        n = len(board[0])
        visited = []
        for i in range(m):
            visited.append([False for j in range(n)])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    f = self.dfs(board,visited,i,j,m,n,word,1)
                    if f:
                        return True
                    visited[i][j] = False
        return False

