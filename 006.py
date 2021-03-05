# -*- coding: utf-8 -*-
# @Time    : 2021-03-04 16:40
# @Author  : zxl
# @FileName: 006.py

import numpy as np

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        loop_len = numRows*2-2 # 这里需要注意
        arr = np.zeros((loop_len+1,))
        for i in range(numRows):
            arr[i] = i
            arr[len(arr)-i-1] = i
        arr = arr[:-1]

        lst = []
        for i in range(numRows):
            lst.append('')

        for i in range(len(s)):
            c = s[i]
            idx = int(arr[i%loop_len])
            lst[idx]+=c
        res = ''
        for i in range(numRows):
            res+=lst[i]
        return res

obj = Solution()
s = "PAYPALISHIRING"
numRows = 4

res = obj.convert(s,numRows)
print(res)

