# -*- coding: utf-8 -*-
# @Time    : 2021-03-08 22:53
# @Author  : zxl
# @FileName: 150.py


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        lst = []
        for item in tokens:
            if item != '+' and item != '-' and item != '*' and item != '/':
                lst.insert(0,int(item))
            else:
                m1 = lst.pop(0)
                m2 = lst.pop(0)
                if item == '+':
                    m = m1 + m2
                elif item == '-':
                    m = m2 - m1
                elif item == '*':
                    m = m1 * m2
                else:
                    m = m2/m1
                lst.insert(0,int(m))
        if len(lst) == 0:
            return 0
        else:
            return lst[0]

obj = Solution()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# 输出: 22
res = obj.evalRPN(tokens)
print(res)