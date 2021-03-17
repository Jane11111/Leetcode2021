# -*- coding: utf-8 -*-
# @Time    : 2021-03-13 21:10
# @Author  : zxl
# @FileName: 130.py

class Solution(object):

    def getNeighbors(self,x,y,m,n):
        neighbors = []
        if x-1 >= 0:
            neighbors.append([x-1,y])
        if x+1 <= m-1:
            neighbors.append([x+1,y])
        if y-1 >= 0:
            neighbors.append([x,y-1])
        if y+1 <= n-1:
            neighbors.append([x,y+1])
        return neighbors

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """


        m = len(board)
        n = len(board[0])

        if m == 1 or n == 1:
            return

        Q = []
        for x in [0,m-1]:
            for y in range(n):
                if board[x][y] == 'O':
                    Q.append([x,y])
                    board[x][y] = 'Y'
        for x in range(1,m-1):
            for y in [0,n-1]:
                if board[x][y] == 'O':
                    Q.append([x,y])
                    board[x][y] = 'Y'
        while len(Q) != 0:

            pos = Q.pop(0)
            neighbors = self.getNeighbors(pos[0],pos[1],m,n)
            for neighbor in neighbors:
                if board[neighbor[0]][neighbor[1]] == 'O':
                    board[neighbor[0]][neighbor[1]] = 'Y'
                    Q.append(neighbor)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'Y':
                    board[i][j] = 'O'


board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
obj = Solution()
obj.solve(board)
print(board)





