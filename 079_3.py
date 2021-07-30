# -*- coding: utf-8 -*-
# @Time    : 2021-07-17 21:13
# @Author  : zxl
# @FileName: 079_3.py

class Solution:

    def dfs(self, dic,visited,word,idx,lastx,lasty):

        if idx==len(word):
            return True

        if word[idx] not in dic:
            return False


        pos = dic[word[idx]]
        for x,y in pos:
            if visited[x][y] :
                continue

            if lastx == -1 or (abs(lastx-x)+abs(lasty-y) == 1):
                visited[x][y] = True
                f = self.dfs(dic,visited,word,idx+1,x,y)
                if f:
                    return f
                visited[x][y] = False
        return False


    def exist(self, board , word: str) -> bool:

        dic  = {}
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                c = board[i][j]
                if c not in dic:
                    dic[c] = []
                dic[c].append([i,j])

        visited = []
        for i in range(m):
            visited.append([False for j in range(n)])

        f = self.dfs(dic,visited,word,0,-1,-1)
        return f



