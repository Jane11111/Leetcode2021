# -*- coding: utf-8 -*-
# @Time    : 2021-04-14 22:11
# @Author  : zxl
# @FileName: 1201_2.py


class Solution:

    def gcd(self,a,b):
        a,b = max(a,b),min(a,b)

        while b:
            c = a%b
            a = b
            b = c
        return a
    def lcm(self,a,b):
        return a*b/self.gcd(a,b)

    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:

        lo = min(a,b,c)
        hi = lo*n

        ab = self.lcm(a,b)
        ac = self.lcm(a,c)
        bc = self.lcm(b,c)
        abc = self.lcm(ab,c)

        while lo < hi:

            m = int((lo+hi)/2)

            if (m//a+m//b+m//c-m//ab-m//ac-m//bc+m//abc)<n:
                lo = m+1
            else:
                hi = m
        return lo


obj = Solution()
n = 1000000000
a = 2
b = 217983653
c = 336916467
ans = obj.nthUglyNumber(n,a,b,c)
print(ans)