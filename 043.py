# -*- coding: utf-8 -*-
# @Time    : 2021-04-16 15:12
# @Author  : zxl
# @FileName: 043.py


class Solution:

    def single_multiply(self,a,b):

        ans = ''
        base = 0
        b = int(b)
        for i in range(len(a)-1,-1,-1):
            v = int(a[i])*b + base
            base = v//10
            ans = str(v%10)+ans
        if base > 0:
            ans = str(base) +ans
        return ans

    def str_add(self,num1,num2):
        if num1 == '':
            return num2
        if num2 == '':
            return num1

        ans = ''
        i = len(num1)-1
        j = len(num2)-1
        base = 0
        while i>=0 or j>=0:
            if i<0:
                c1 = 0
            else:
                c1 = int(num1[i])
                i-=1
            if j<0:
                c2 = 0
            else:
                c2 = int(num2[j])
                j-=1
            n = c1+c2+base
            base = n//10
            ans = str(n%10)+ans
        if base>0:
            ans = str(base) + ans

        return ans


    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'


        if len(num1)<len(num2):
            num1,num2 = num2,num1

        base = ''
        ans = ''
        for i in range(len(num2)-1,-1,-1):
            c = num2[i]
            m = self.single_multiply(num1,c)
            m= m+base
            base = base+'0'
            ans = self.str_add(m,ans)
        return ans


obj  = Solution()
num1 = '123'
num2 = '0'
ans = obj.multiply(num1,num2)
print(ans)