# -*- coding: utf-8 -*-
# @Time    : 2021-06-25 13:18
# @Author  : zxl
# @FileName: 419.py


class Solution:
    def countBattleships(self, board ) -> int:


        ans = 0

        m = len(board)
        n = len(board[0])


        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and ((i-1<0 or board[i-1][j] == '.') and (j-1<0 or board[i][j-1] == '.')):
                    ans+=1

        return ans

