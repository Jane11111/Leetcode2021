# -*- coding: utf-8 -*-
# @Time    : 2021-03-15 14:22
# @Author  : zxl
# @FileName: 091.py


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s[0] == '0':
            return 0

        arr = [0 for i in range(len(s))]
        arr[0] = 1
        for i in range(1,len(s)):

            if arr[i-1] == 0:
                arr[i] = 0
                continue

            if s[i-1] == '0':

                if s[i] == '0':
                    arr[i] = 0
                    continue
                if i == 1:
                    arr[i] = 0
                elif i==2:
                    arr[i] = 1
                else:
                    arr[i] = arr[i-3]
                continue

            if s[i] == '0'  :
                if s[i-1] + s[i] >'26':
                    arr[i] = 0
                elif i==1:
                    arr[i ] = 1
                else:
                    arr[i] = arr[i-2]
            elif  s[i-1]+s[i] >'26':
                arr[i] = arr[i-1]
            else:
                num = arr[i-1]
                num+= arr[i-2] if i>1 else 1
                arr[i] = num
        return arr[len(s)-1]

obj = Solution()
s = "230"
ans = obj.numDecodings(s)
print(ans)