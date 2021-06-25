# -*- coding: utf-8 -*-
# @Time    : 2021-06-23 14:35
# @Author  : zxl
# @FileName: 400.py

class Solution:
    def findNthDigit(self, n: int) -> int:

        if n<=9:
            return n

        i = 1

        while True:

            cur_count = 9*(10**(i-1))*i

            if n<=cur_count:
                break
            n-=cur_count
            i+=1

        a,b = n//i, n%i

        num = 10**(i-1)+a
        if not b:
            num -= 1


        lst = []
        while num:
            lst.insert(0,num%10)
            num//=10
        return lst[b-1]




obj = Solution()
n = 15
ans = obj.findNthDigit(n)
print(ans)




