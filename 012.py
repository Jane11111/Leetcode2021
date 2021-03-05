# -*- coding: utf-8 -*-
# @Time    : 2021-03-04 20:53
# @Author  : zxl
# @FileName: 012.py

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        arr = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        dic = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',
               10:'X',9:'IX',5:'V',4:'IV',1:'I'}
        res = ''
        for item in arr:
            n = int(num/item)
            num = num%item

            for i in range(n):
                res += dic[item]
        return res

obj = Solution()
num = 1994
res = obj.intToRoman(num)
print(res)