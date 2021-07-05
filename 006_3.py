# -*- coding: utf-8 -*-
# @Time    : 2021-07-05 10:36
# @Author  : zxl
# @FileName: 006_3.py


class Solution:
    def convert(self, s: str, numRows: int) -> str:



        if numRows == 1:
            return s
        ans = ''
        for r in range(numRows):

            below_space = (numRows-r-1)*2
            up_space = r*2

            spaces = [below_space,up_space]
            i = r
            cur_space = 1
            while i<len(s):

                ans += s[i]



                cur_space = (cur_space+1)%2
                while spaces[cur_space] == 0:
                    cur_space = (cur_space + 1) % 2

                i += spaces[cur_space]



        return ans

