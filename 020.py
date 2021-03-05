# -*- coding: utf-8 -*-
# @Time    : 2021-03-02 10:25
# @Author  : zxl
# @FileName: 020.py

class Solution(object):

    def isMatch(self,a,b):
        if (a=='(' and b==')') or (a=='[' and b == ']') or (a=='{' and b=='}'):
            return True
        else:
            return False

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = ''

        for c in s:
            if len(stack) == 0:
                stack+=c
            else:
                if self.isMatch(stack[len(stack)-1],c):
                    stack = stack[:len(stack)-1]
                else:
                    stack += c

        if len(stack) == 0:
            return True
        else:
            return False



obj = Solution()
s = '([)]'
res = obj.isValid(s)
print(res)