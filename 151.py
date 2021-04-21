# -*- coding: utf-8 -*-
# @Time    : 2021-04-19 11:52
# @Author  : zxl
# @FileName: 151.py


class Solution:
    def reverseWords(self, s: str) -> str:

        arr = s.split( )
        new_str = ''
        for i in range(len(arr)-1,-1,-1):
            word = arr[i]
            new_str = new_str + word
            if i != 0:
                new_str += ' '

        return new_str

obj = Solution()
s = "  hello world  "
ans = obj.reverseWords(s)
print(ans)