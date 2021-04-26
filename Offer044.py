# -*- coding: utf-8 -*-
# @Time    : 2021-04-24 22:44
# @Author  : zxl
# @FileName: Offer044.py



class Solution:
    def findNthDigit(self, n: int) -> int:
        n+=1

        if n<=10:
            return n-1


        base = 1
        num = 10
        last_num = 0
        while n>num:
            base+=1
            last_num = num
            num+=base*9*(10**(base-1))

        n-=last_num
        a = n//base # 第几个数
        b = n%base #第几位

        if not(a==0 and b==0):
            a-=1
            a+=int(b>0)

        # num = 9*10**(base-2)+a
        num = 10**(base-1)+a

        lst = []
        while num:
            lst.insert(0,num%10)
            num //=10
        return lst[b-1]






obj = Solution()
n = 999999999
ans = obj.findNthDigit(n)
print(ans)