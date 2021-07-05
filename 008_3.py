# -*- coding: utf-8 -*-
# @Time    : 2021-07-05 10:56
# @Author  : zxl
# @FileName: 008_3.py



class Solution:
    def myAtoi(self, s: str) -> int:


        i = 0
        while i<len(s) and s[i] == ' ':
            i+=1

        op = '+'
        if i<len(s) and (s[i] == '+' or s[i] == '-'):
            op = s[i]
            i+=1



        num_str = ''

        while i<len(s) and s[i].isdigit():
            num_str+=s[i]
            i+=1

        i = 0
        while i<len(num_str) and num_str[i] == '0':
            i+=1
        num_str = num_str[i:]

        if len(num_str) == 0:
            return 0

        if len(num_str)>10:
            if op == '+':
                return 2**31-1
            return -2**31

        num = int(num_str)
        if op == '-':
            num = -num
        if num > 2**31-1:
            num = 2**31-1
        if num < -2**31:
            num = -2**31
        return num



