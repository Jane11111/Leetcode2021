# -*- coding: utf-8 -*-
# @Time    : 2021-04-25 21:20
# @Author  : zxl
# @FileName: 233.py



class Solution:
    def countDigitOne(self, n: int) -> int:


        i = 1
        count = 0
        num = n

        while n:
            if n%10 == 0:
                count+= (n//10)*i
            if n%10 == 1:
                count+=(n//10)*i+1+num%i
            if n%10 >1:
                count += ((n//10)+1)*i

            n//=10
            i*=10
        return count

obj = Solution()
n = 21
ans = obj.countDigitOne(n)
print(ans)