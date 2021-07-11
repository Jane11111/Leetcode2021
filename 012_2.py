# -*- coding: utf-8 -*-
# @Time    : 2021-07-07 11:34
# @Author  : zxl
# @FileName: 012_2.py

class Solution:
    def intToRoman(self, num: int) -> str:

        dic = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M',
               4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM'}

        lst = [1000,900,500,400,100,90,50,40,10,9,5,4,1]

        s = ''
        while num>0:

            for item in lst:
                if num//item:

                    s+=dic[item]*(num//item)

                    num = num%item
        return s

