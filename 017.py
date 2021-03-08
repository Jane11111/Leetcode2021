# -*- coding: utf-8 -*-
# @Time    : 2021-03-05 21:41
# @Author  : zxl
# @FileName: 017.py

class Solution(object):

    def recursiveCombine(self,digits,dic):
        res = []
        if len(digits) == 0:
            return res
        if len(digits) == 1:
            return dic[digits[0]]
        sub_res = self.recursiveCombine(digits[1:],dic)
        for c1 in dic[digits[0]]:
            for c2 in sub_res:
                res.append(c1+c2)
        return res

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {'2':['a','b','c'],
               '3':['d','e','f'],
               '4':['g','h','i'],
               '5':['j','k','l'],
               '6':['m','n','o'],
               '7':['p','q','r','s'],
               '8':['t','u','v'],
               '9':['w','x','y','z']}
        res = self.recursiveCombine(digits,dic)
        return res

