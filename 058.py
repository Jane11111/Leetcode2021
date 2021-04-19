# -*- coding: utf-8 -*-
# @Time    : 2021-04-17 22:12
# @Author  : zxl
# @FileName: 058.py


class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        count = 0

        i = len(s)-1
        while i>=0 and s[i]==' ':
            i-=1

        for i in range(i,-1,-1):
            if s[i] == ' ':
                return count
            count+=1
        return count

obj = Solution()
s = 'a '
ans = obj.lengthOfLastWord(s)
print(ans)