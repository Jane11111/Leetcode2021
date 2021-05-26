# -*- coding: utf-8 -*-
# @Time    : 2021-05-26 20:18
# @Author  : zxl
# @FileName: 306_2.py


class Solution:


    def str_add(self,s1,s2):

        new_s = ''
        base = 0
        i = len(s1)-1
        j = len(s2) - 1
        while i>=0 or j>=0 :
            if i<0:
                n1 = 0
            else:
                n1 = int(s1[i])
            if j<0:
                n2 = 0
            else:
                n2 = int(s2[j])
            v = n1+n2+base
            base = v//10
            v%=10
            new_s = str(v)+new_s
            i-=1
            j-=1
        if base:
            new_s = str(base)+new_s
        return new_s


    def recFind(self,num,i,last_num1,last_num2):

        if i>=len(num):
            return True
        # if num[i] == '0':
        #     return False

        s_sum_val = self.str_add(last_num1,last_num2)

        if num[i:i+len(s_sum_val)] != s_sum_val:
            return False
        return self.recFind(num,i+len(s_sum_val),last_num2,s_sum_val)

    def isAdditiveNumber(self, num: str) -> bool:


        for i in range(len(num)):
            last_num1 = num[:i+1]
            for j in range(i+1,len(num)):

                if (num[i+1] == '0' and j-i>1) or j+1>=len(num):
                    break

                last_num2 = num[i+1:j+1]
                f = self.recFind(num,j+1,last_num1,last_num2)
                if f:
                    return True
        return False

obj = Solution()
num = "101020305080130210"

ans = obj.isAdditiveNumber(num)
print(ans)
