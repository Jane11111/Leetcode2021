# -*- coding: utf-8 -*-
# @Time    : 2021-06-04 14:26
# @Author  : zxl
# @FileName: 022_2.py



class Solution:


    def recSolve(self,left_num,right_num,s,lst):

        if left_num == 0 and right_num == 0:
            lst.append(s)
            return

        if left_num == 0:
            self.recSolve(left_num,right_num-1,s+')',lst)
            return

        if left_num == right_num:
            self.recSolve(left_num-1,right_num,s+'(',lst)
        elif left_num<right_num:
            self.recSolve(left_num-1,right_num,s+'(',lst)
            self.recSolve(left_num,right_num-1,s+')',lst)





    def generateParenthesis(self, n: int) :


        ans = []
        self.recSolve(n,n,'',ans)
        return ans


