# -*- coding: utf-8 -*-
# @Time    : 2021-07-26 12:03
# @Author  : zxl
# @FileName: 76_3.py




class Solution:
    def minWindow(self, s: str, t: str) -> str:

        tdic = {}
        tcount = 0
        for c in t:
            if c not in tdic:
                tcount+=1
                tdic[c] = 0
            tdic[c]+=1

        sdic = {}
        scount = 0
        p = 0
        ans = ''
        for i in range(len(s)):

            c = s[i]
            if c not in sdic:
                sdic[c] = 0
            sdic[c] += 1

            if c in tdic and sdic[c] == tdic[c]: # 有一个字母满足了条件
                scount +=1

            if scount == tcount:
                while scount == tcount:
                    sdic[s[p]]-=1
                    if s[p] in tdic and sdic[s[p]]<tdic[s[p]]: # 因为减去p，使得字母数量不够了
                        scount-=1
                    p+=1
                if ans == '' or i-p+2<len(ans):
                    ans = s[p-1:i+1]
        return ans

obj = Solution()
s = "cabwefgewcwaefgcf"
t = "cae"
ans = obj.minWindow(s,t)
print(ans)


