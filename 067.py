# -*- coding: utf-8 -*-
# @Time    : 2021-04-18 12:40
# @Author  : zxl
# @FileName: 067.py

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        base = 0
        i = len(a)-1
        j = len(b) -1
        ans = ''
        while i>=0 or j>=0:
            if i<0:
                c1= 0
            else:
                c1 = int(a[i])
            if j<0:
                c2 = 0
            else:
                c2 = int(b[j])
            i-=1
            j-=1

            v = c1+c2 +base
            ans = str(v%2)+ans
            base = v//2
        if base!=0:
            ans = str(base)+ans
        return ans

obj = Solution()
a = "1010"
b = "1011"
ans = obj.addBinary(a,b)
print(ans)



