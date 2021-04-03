# -*- coding: utf-8 -*-
# @Time    : 2021-03-26 14:50
# @Author  : zxl
# @FileName: 044.py

# TODO 超时

class Solution(object):

    def recursiveMatch(self,s,p,i,j):
        if i == len(s) :
            if j == len(p):
                return True
            else:
                if p[j] == '*':
                    return self.recursiveMatch(s,p,i,j+1)
                else:
                    return False
        elif j==len(p):
            return False

        if p[j] == '?':
            return self.recursiveMatch(s,p,i+1,j+1)
        elif p[j] == '*':
            for k in range(i,len(s)+1):
                f = self.recursiveMatch(s,p,k,j+1)
                if f:
                    return f
        else:
            if s[i] == p[j]:
                return self.recursiveMatch(s,p,i+1,j+1)
            else:
                return False
        return False



    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        new_pattern = ''
        for i in range(len(p)):
            if len(new_pattern) == 0:
                new_pattern+=p[i]
            else:
                if p[i] == '*' and p[i-1] == '*':
                    continue
                else:
                    new_pattern += p[i]

        f = self.recursiveMatch(s,new_pattern,0,0)
        return f

obj = Solution()
s="aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba"
p="a*******b"
f = obj.isMatch(s,p)
print(f)

