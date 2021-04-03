# -*- coding: utf-8 -*-
# @Time    : 2021-04-01 23:04
# @Author  : zxl
# @FileName: 402.py


class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        if len(num) == k:
            return '0'
        lst = []
        c = 0
        for n in num:

            while c<k and lst and lst[-1]>n:
                lst.pop(-1)
                c+=1
            lst.append(n)
        while c<k:
            lst.pop(-1)
            c+=1
        s_num = ''.join(lst)
        i = 0
        while i< len(s_num) and s_num[i] == '0':
            i+=1
        if i == len(s_num):
            return '0'
        else:
            return s_num[i:]

obj = Solution()
num = "10"
k = 2
ans = obj.removeKdigits(num,k)
print(ans)