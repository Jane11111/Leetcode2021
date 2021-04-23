# -*- coding: utf-8 -*-
# @Time    : 2021-04-21 17:15
# @Author  : zxl
# @FileName: 212.py

# TODO 复杂度跟words长度有关

class Solution:

    def dfs(self,word,visited,pos_dic,i,last_pos):
        if i == len(word):
            return True
        c = word[i]
        if word[i] not in pos_dic:
            return False
        for x,y in pos_dic[word[i]]:
            if  visited[x][y] == False and (x==last_pos[0] and abs(y-last_pos[1])== 1 or y==last_pos[1] and abs(x-last_pos[0])==1) :
                visited[x][y] = True
                f = self.dfs(word,visited,pos_dic,i+1,(x,y))
                visited[x][y] = False
                if f:
                    return f


        return False

    def findWords(self, board , words )  :

        pos_dic = {}
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                c = board[i][j]
                if c not in pos_dic:
                    pos_dic[c] = [[i,j]]
                else:
                    pos_dic[c].append([i,j])
        visited = []
        for i in range(m):
            visited.append([False for j in range(n)])
        ans = []
        for word in words:
            stop = False
            for c in word:
                if c not in pos_dic:
                    stop = True
                    break
            if stop:
                continue



            c = word[0]
            if c not in pos_dic:
                continue

            for x,y in pos_dic[c]:
                visited[x][y] = True
                f = self.dfs(word,visited,pos_dic,1,(x,y))
                visited[x][y] = False
                if f:
                    ans.append(word)
                    break
        return ans

