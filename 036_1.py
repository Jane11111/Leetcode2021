# -*- coding: utf-8 -*-
# @Time    : 2021-07-12 15:15
# @Author  : zxl
# @FileName: 036_1.py




class Solution:
    def isValidSudoku(self, board ) -> bool:



        dic = {str(i+1):[{},{},{}] for i in range(9)}


        for i in range(9):
            for j in range(9):

                if board[i][j] == '.':
                    continue

                box_num = 3*(i//3)+j//3

                num = board[i][j]

                if i in dic[num][0] or j in dic[num][1] or box_num in dic[num][2]:
                    return False
                dic[num][0][i] = True
                dic[num][1][j] = True
                dic[num][2][box_num] = True
        return True

