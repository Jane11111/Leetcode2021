# -*- coding: utf-8 -*-
# @Time    : 2021-07-05 11:20
# @Author  : zxl
# @FileName: 009_3.py



class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x<0:
            return False
        if x<10:
            return True
        num = 0

        while x>0:

            mod =  x%10


            if num == x or num == x//10: # 分别对应奇数和偶数
                return True
            if num == 0 and mod == 0: # 最高位不是0 ，所以最低位也不能为0
                return False

            num= num*10 + mod
            x //= 10

            if num>x:
                return False

        return False
