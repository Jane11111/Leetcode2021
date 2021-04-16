# -*- coding: utf-8 -*-
# @Time    : 2021-04-16 14:23
# @Author  : zxl
# @FileName: 036.py


class Solution:
    def isValidSudoku(self, board )  :

        for i in range(9):
            row_dic = {}
            col_dic = {}
            for j in range(9):
                marker1 = board[i][j]
                marker2 = board[j][i]

                if marker1!='.':
                    if marker1 in row_dic:
                        return False
                    else:
                        row_dic[marker1] = True
                if marker2!='.':
                    if marker2 in col_dic:
                        return False
                    else:
                        col_dic[marker2] = True

        for i in [0,3,6]:
            for j in [0,3,6]:
                dic = {}

                for m1 in range(3):
                    for m2 in range(3):
                        if board[i+m1][j+m2] != '.' and  board[i+m1][j+m2]  in dic:
                            return False
                        dic[board[i+m1][j+m2] ]= True
        return True


obj = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
ans = obj.isValidSudoku(board)
print(ans)
