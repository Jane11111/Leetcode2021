# -*- coding: utf-8 -*-
# @Time    : 2021-07-05 11:33
# @Author  : zxl
# @FileName: 10_3.py

class Solution:

    def recMatch(self,s,p,memo):
        if s in memo and p in memo[s]:
            return memo[s][p]
        if len(s) == 0 and len(p) == 0:
            return True
        if len(p) == 0:
            return False

        if s not in memo:
            memo[s] = {}
        if len(s) == 0:
            i = 1
            while i<len(p) and p[i] == '*':
                i+=2

            f = len(p) >=2 and i==len(p)+1

            memo[s][p] = f
            return f

        if len(p) >1 and p[1] == '*':
            if p[0] == '.' or p[0] == s[0]: # 能匹配
                f1 = self.recMatch(s[1:],p[2:],memo) # 匹配一次
                f2 = self.recMatch(s[1:],p,memo) # 匹配多次
                f3 = self.recMatch(s,p[2:],memo) # 不匹配
                # if s == 'ba' and p == '.*a*a':
                #     print('I AM here')
                f = f1 or f2 or f3
            else:
                f = self.recMatch(s,p[2:],memo)
            memo[s][p] = f

        else:
            f = (s[0] == p[0] or p[0] == '.') and self.recMatch(s[1:],p[1:],memo)
            memo[s][p] = f

        return memo[s][p]



    def isMatch(self, s: str, p: str) -> bool:

        memo = {}
        ans = self.recMatch(s,p,memo)
        return ans

obj = Solution()
s = 'aab'
p = 'c*a*b'
ans = obj.isMatch(s,p)
print(ans)

