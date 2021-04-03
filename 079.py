# -*- coding: utf-8 -*-
# @Time    : 2021-03-26 09:38
# @Author  : zxl
# @FileName: 079.py


class Solution(object):

    def getNeighbor(self,i,j,m,n):
        neighbors = []
        if i-1>=0:
            neighbors.append((i-1,j))
        if i+1<m:
            neighbors.append((i+1,j))
        if j-1>=0:
            neighbors.append((i,j-1))
        if j+1<n:
            neighbors.append((i,j+1))
        return neighbors

    def recursiveExist(self,board,judge,word,i,j,p):

        if p == len(word) or (p==len(word)-1 and i<len(board) and word[p] == board[i][j]):
            return True
        m = len(board)
        n = len(board[0])

        if i>=m:
            return False

        s = word[p]
        if board[i][j]!=s:
            return False

        # if p == len(word)-1:
        #     return True

        neighbors = self.getNeighbor(i,j,m,n)
        for x,y in neighbors:
            if judge[x][y] == 0:
                judge[x][y] = 1
                f = self.recursiveExist(board,judge,word,x,y,p+1)
                judge[x][y] = 0
                if f:
                    return f
        return False


    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        if len(word) == 0:
            return True

        m = len(board)
        n = len(board[0])
        judge = []
        for i in range(m):
            arr = []
            for j in range(n):
                arr.append(0)
            judge.append(arr)

        for i in range(m):
            for j in range(n):
                if board[i][j] != word[0]:
                    continue
                judge[i][j] = 1
                f = self.recursiveExist(board,judge,word,i,j,0)
                judge[i][j] = 0
                if f:
                    return f
        return False

obj = Solution()
board =[["a","b"],["c","d"]]
word = "cdba"
ans = obj.exist(board,word)
print(ans)
