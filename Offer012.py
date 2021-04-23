# -*- coding: utf-8 -*-
# @Time    : 2021-04-23 10:05
# @Author  : zxl
# @FileName: Offer012.py

class Solution:

    def is_neighbors(self,x,y,last_x,last_y):
       return  ((x == last_x and abs(y - last_y) == 1) or (y == last_y and abs(x - last_x) == 1))

    def dfs(self,dic,word,i,visited,last_x,last_y):
        if i == len(word):
            return True
        c = word[i]
        if c not in dic:
            return False

        for x,y in dic[c]:
            if (not visited[x][y]) and (self.is_neighbors(x,y,last_x,last_y) or (last_x==-1 and last_y == -1)):
                visited[x][y] = True
                f = self.dfs(dic,word,i+1,visited,x,y)
                visited[x][y] = False
                if f:
                    return f
        return False

    def exist(self, board , word )  :

        m = len(board)
        n = len(board[0])
        dic = {}
        for i in range(m):
            for j in range(n):
                if board[i][j] not in dic:
                    dic[board[i][j]] = [[i,j]]
                else:
                    dic[board[i][j]].append([i,j])
        visited = []
        for  i in range(m):
            visited.append([False for j in range(n)])

        f = self.dfs(dic,word,0,visited,-1,-1)
        return f



