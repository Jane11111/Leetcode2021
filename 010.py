# -*- coding: utf-8 -*-
# @Time    : 2021-04-28 16:57
# @Author  : zxl
# @FileName: 010.py

class Solution:

    def recursiveMatch(self,s,p,i,j,dic):
        if i == len(s) and j == len(p):
            return True
        if j == len(p):
            return False
        if i == len(s):
            while j+1<len(p) and p[j+1] == '*':
                j+=2
            return j==len(p)
        if i in dic and j in dic[i]:
            return dic[i][j]

        if i not in dic:
            dic[i] = {}
        if j+1<len(p) and p[j+1] == '*':

            if p[j] == '.' or p[j] == s[i]:
                f1 = self.recursiveMatch(s,p,i+1,j+2,dic) # 匹配1个
                if i+1 not in dic:
                    dic[i+1] = {}
                dic[i+1][j+2] = f1

                if f1:
                    return True

                f2 = self.recursiveMatch(s,p,i+1,j,dic) # 匹配多个
                dic[i + 1][j] = f2
                if f2:
                    return True

                f3 = self.recursiveMatch(s,p,i,j+2,dic) # 匹配0个
                dic[i][j + 2] = f3
                if f3:
                    return True

                return False

            else:
                f = self.recursiveMatch(s,p,i,j+2,dic)
                dic[i][j+2] = f
                return f
        else:
            if p[j] == '.' or p[j] == s[i]:
                f =  self.recursiveMatch(s,p,i+1,j+1,dic)
                if i+1 not in dic:
                    dic[i+1] = {}
                dic[i+1][j+1] = f
                return f
            else:
                dic[i][j]=False
                return False




    def isMatch(self, s: str, p: str) -> bool:

        return self.recursiveMatch(s,p,0,0,{})

obj = Solution()
s="aaaaaaaaaaaaab"
p="a*a*a*a*a*a*a*a*a*a*a*a*b"
ans = obj.isMatch(s,p)
print(ans)









