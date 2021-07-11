# -*- coding: utf-8 -*-
# @Time    : 2021-07-07 17:26
# @Author  : zxl
# @FileName: 022_4.py





class Solution:
    def generateParenthesis(self, n: int):


        ans = ['(']
        lst = [1]

        for i in range(2,2*n+1):
            l = len(ans)
            for j in range(l):
                s = ans.pop(0)
                left_count = lst.pop(0)
                right_count = len(s)-left_count

                if left_count == right_count:
                    ans.append(s+'(')
                    lst.append(left_count+1)
                else:
                    ans.append(s + ')')
                    lst.append(left_count )
                    if left_count < n:
                        ans.append(s + '(')
                        lst.append(left_count + 1)
        return ans
