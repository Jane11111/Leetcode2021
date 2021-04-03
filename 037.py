# -*- coding: utf-8 -*-
# @Time    : 2021-03-25 17:00
# @Author  : zxl
# @FileName: 037.py


class Solution(object):

    def getNextPos(self,i,j,n):
        if j+1 == n:
            return (i+1,0)
        return (i,j+1)

    def getPossibleValues(self,board,i,j,n):

        dic = {str(i):True for i in range(1,n+1)}

        for k in range(n):
            s = board[i][k]
            if s != '.':
                dic[s] = False
            s = board[k][j]
            if s != '.':
                dic[s] = False
        for k1 in range(i-1,i+2):
            for k2 in range(j-1,j+2):
                if k1 < 0 or k1>=n or k2<0 or k2>=n:
                    continue
                s = board[k1][k2]
                if s != '.':
                    dic[s] = False
        lst = []
        for k in dic:
            if dic[k]:
                lst.append(k)
        return lst



    def recursiveSolve(self,board,i,j):
        n = len(board)
        if i>=n:
            return True
        # print(i,j)
        next_i, next_j = self.getNextPos(i,j,n)
        if board[i][j] != '.':
            return self.recursiveSolve(board,next_i,next_j)


        possible_values = self.getPossibleValues(board,i,j,n)
        for v in possible_values:

            board[i][j] = v
            f = self.recursiveSolve(board,next_i,next_j)
            # if i==0 and j == 2 and v == '4':
            #     print(f)
            if f :
                return True
            board[i][j] = '.'
        # print(i,j)
        return False





    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        return self.recursiveSolve(board,0,0)


obj = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

ans = obj.solveSudoku(board)
print(board)
print(ans)


