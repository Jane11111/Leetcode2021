# -*- coding: utf-8 -*-
# @Time    : 2021-04-14 13:58
# @Author  : zxl
# @FileName: I0814.py


class Solution:

    def recursiveCount(self,s,dic,result):
        if s in dic and result in dic[s]:
            return dic[s][result]


        if len(s) == 0:
            return 0
        if len(s) == 1 :
            return int(int(s) == result)
        ans = 0
        for i in range(1,len(s),2):
            l = s[:i]
            r = s[i+1:]
            ops = s[i]
            if ops == '&':
                if result == 1:
                    ans +=  self.recursiveCount(l,dic,1) * self.recursiveCount(r,dic,1)
                else:
                    ans +=  self.recursiveCount(l,dic,0) * self.recursiveCount(r,dic,1)+\
                           self.recursiveCount(l,dic,1) * self.recursiveCount(r,dic,0)+\
                           self.recursiveCount(l,dic,0) * self.recursiveCount(r,dic,0)
            elif ops == '|':
                if result == 1:
                    ans += self.recursiveCount(l, dic, 0) * self.recursiveCount(r, dic, 1) + \
                          self.recursiveCount(l, dic, 1) * self.recursiveCount(r, dic, 0)+ \
                          self.recursiveCount(l, dic, 1) * self.recursiveCount(r, dic, 1)
                else:
                    ans += self.recursiveCount(l, dic, 0) * self.recursiveCount(r, dic, 0)
            elif ops == '^':
                if result == 1:
                    ans += self.recursiveCount(l, dic, 0) * self.recursiveCount(r, dic, 1) + \
                          self.recursiveCount(l, dic, 1) * self.recursiveCount(r, dic, 0)
                else:
                    ans += self.recursiveCount(l, dic, 0) * self.recursiveCount(r, dic, 0) + \
                          self.recursiveCount(l, dic, 1) * self.recursiveCount(r, dic, 1)
        if s not in dic:
            dic[s] = {}
        dic[s][result] = ans
        return ans




    def countEval(self, s: str, result: int) -> int:
        ans = self.recursiveCount(s,{},result)
        return ans





obj = Solution()
s = "0&0&0&1^1|0"
result = 1

ans = obj.countEval(s,result)
print(ans)


