# -*- coding: utf-8 -*-
# @Time    : 2021-07-12 17:19
# @Author  : zxl
# @FileName: 043_1.py


class Solution:

    def stradd(self,num1,num2):


        s = ''
        base = 0

        i = len(num1)-1
        j = len(num2)-1

        while i>=0 or j>=0:

            if i<0:
                n1 = 0
            else:
                n1 = int(num1[i])

            if j<0:
                n2 = 0
            else:
                n2 = int(num2[j])
            i-=1
            j-=1
            n = n1+n2+base

            base = n//10
            s = str(n%10)+s
        if base:
            s = str(base)+s
        return s

    def strmul(self,num1,num2):

        s = ''

        base = 0
        n1 = int(num1)

        i = len(num2)-1
        while i>=0:
            n2 = int(num2[i])
            n = n1*n2+base

            base = n//10
            s = str(n%10)+s
            i-=1
        if base:
            s = str(base)+s
        return s


    def multiply(self, num1: str, num2: str) -> str:

        if num1 == '0' or num2 == '0':
            return '0'



        if len(num1)>len(num2):
            return self.multiply(num2,num1)

        count = 0
        ans = '0'

        for i in range(len(num1)-1,-1,-1):
            n1 = num1[i]

            cur_s = self.strmul(n1,num2)
            cur_s += '0'*count

            ans = self.stradd(ans,cur_s)
            count+=1
        return ans




