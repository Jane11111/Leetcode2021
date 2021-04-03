# -*- coding: utf-8 -*-
# @Time    : 2021-03-26 10:15
# @Author  : zxl
# @FileName: 079_2.py



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

    def recursiveExist(self,board,word,i,j,p):

        if p == len(word)-1 :
            return True
        m = len(board)
        n = len(board[0])

        if i>=m:
            return False


        neighbors = self.getNeighbor(i,j,m,n)
        for x,y in neighbors:
            if board[x][y] != '*' and board[x][y] == word[p+1]:
                s = board[x][y]
                board[x][y] = '*'
                f = self.recursiveExist(board,word,x,y,p+1)
                board[x][y] = s
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

        for i in range(m):
            for j in range(n):
                if board[i][j] != word[0]:
                    continue
                s = board[i][j]
                board[i][j] = '*'
                f = self.recursiveExist(board,word,i,j,0)
                board[i][j] = s
                if f:
                    return f
        return False

obj = Solution()
board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCB"
ans = obj.exist(board,word)
print(ans)