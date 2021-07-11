# -*- coding: utf-8 -*-
# @Time    : 2021-07-07 17:14
# @Author  : zxl
# @FileName: 022_3.py



class Solution:


    def recGenerate(self,left_count,right_count,n,s,ans):

        if len(s) == 2*n:
            ans.append(s)
            return

        if left_count == right_count:
            self.recGenerate(left_count+1,right_count,n,s+'(',ans)
        else:

            self.recGenerate(left_count,right_count+1,n,s+')',ans)
            if left_count < n:
                self.recGenerate(left_count+1, right_count, n, s + '(', ans)



    def generateParenthesis(self, n: int) :


        ans = []
        self.recGenerate(0,0,n,'',ans)
        return ans

