# -*- coding: utf-8 -*-
# @Time    : 2021-04-22 22:52
# @Author  : zxl
# @FileName: Offer005.py



class Solution:
    def replaceSpace(self, s: str) -> str:

        new_s = ''
        for c in s:
            if c == ' ':
                new_s+='%20'
            else:
                new_s+=c
        return new_s