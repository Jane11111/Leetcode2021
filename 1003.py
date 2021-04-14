# -*- coding: utf-8 -*-
# @Time    : 2021-04-07 14:17
# @Author  : zxl
# @FileName: 1003.py


class Solution:
    def isValid(self, s: str) -> bool:

        lst = []
        for c in s:
            if c == 'c':
                if len(lst) >= 2 and lst[-1] == 'b' and lst[-2] == 'a':
                    lst.pop()
                    lst.pop()
                else:
                    return False
            else:
                lst.append(c)
        return len(lst) == 0

obj = Solution()
s = "cababc"
ans = obj.isValid(s)
print(ans)