# -*- coding: utf-8 -*-
# @Time    : 2021-07-17 20:42
# @Author  : zxl
# @FileName: 076_2.py


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        sdic= {}
        tdic = {}

        for i in range(26):
            c1 = chr(i+ord('a'))
            c2 = chr(i+ord('A'))
            sdic[c1] = 0
            sdic[c2] = 0
            tdic[c1] = 0
            tdic[c2] = 0

        num = 0
        for c in t:
            tdic[c] += 1
            if tdic[c] == 1:
                num+=1

        count = 0
        idx = -1
        ans = ''
        for i in range(len(s)):
            c = s[i]

            sdic[c] += 1
            if sdic[c] == tdic[c]:
                count+=1

            while count == num:

                if i-idx<len(ans) or ans == '':
                    ans = s[idx+1:i+1]
                idx+=1
                sdic[s[idx]]-=1
                if sdic[s[idx]] < tdic[s[idx]]:
                    count-=1
        return ans

obj = Solution()
s = "a"
t = "aa"
ans = obj.minWindow(s,t)
print(ans)


