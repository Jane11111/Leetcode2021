# -*- coding: utf-8 -*-
# @Time    : 2021-03-25 20:29
# @Author  : zxl
# @FileName: 306.py


class Solution(object):

    def isAdditiveNumberWithBase(self,num,base1,base2):


        if len(num)==0  or (base1[0] == '0' and len(base1) >1) or (base2[0] == '0'and len(base2) > 1):
            return False

        val = str(int(base1)+int(base2))
        if val == num:
            return True

        if num[:len(val)] == val:
            return self.isAdditiveNumberWithBase(num[len(val):],base2,val)
        return False



    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """

        for i in range(1,len(num)):
            for j in range(i+1,len(num)+1):
                base1 = num[:i]
                base2 = num[i:j]
                f = self.isAdditiveNumberWithBase(num[j:],base1,base2)
                if f:
                    return f
        return False

obj = Solution()
num =  "101"
ans = obj.isAdditiveNumber(num)
print(ans)
