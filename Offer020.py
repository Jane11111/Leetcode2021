# -*- coding: utf-8 -*-
# @Time    : 2021-06-14 11:26
# @Author  : zxl
# @FileName: Offer020.py



class Solution:

    def isInteger(self,s):
        i = 0
        while i<len(s) and s[i] == ' ':
            i+=1

        if i<len(s) and (s[i] == '+' or s[i] == '-'):
            i+=1

        j = len(s)-1

        while j>=0 and s[j] == ' ':
            j-=1

        f = i<=j

        while i<=j:
            if not s[i].isdigit():
                f = False
                break
            i+=1
        return f
    def onlyOp(self,s):

        op_count = 0
        for c in s:
            if c == '+' or c == '-':
                op_count+=1
            elif c!= ' ' and not c.isdigit():
                return False
        return op_count ==1

    def isEmpty(self,s):

        for c in s:
            if c!= ' ':
                return False
        return True

    def isNumber(self, s: str) -> bool:


        dot_count = 0
        dot_idx = -1
        e_count = 0
        e_idx = -1
        op_count = 0
        for i in range(len(s)):
            c = s[i]
            if c == 'e' or c== 'E':
                e_count+=1
                e_idx = i
            elif c == '.':
                dot_count +=1
                dot_idx = i
            elif c == '+' or c == '-':
                op_count+=1
            elif not(c== ' ' or c.isdigit()):
                return False
        if e_count>1 or dot_count>1 or op_count >2 or (e_idx!= -1 and dot_idx!=-1 and e_idx<dot_idx):
            return False

        f1 = True
        f2 = True
        f3 = True
        if dot_count== 1:
            s1 = s[:dot_idx]
            s2 = s[dot_idx+1: len(s) if e_idx==-1 else e_idx]


            f5 = self.isEmpty(s1)
            f6 = self.isEmpty(s2)
            if (f5 and f6) or (not f6 and s2[0] == ' ') or (not f5 and s1[-1] == ' ') or ('+' in s2 or '-' in s2):
                f1 = False
            else:

                f1 = self.isInteger(s1) or f5
                f2 = self.isInteger(s2) or f6
                if not f1  and self.onlyOp(s1) and not f6:
                    f1 = True


        else:
            s1 = s[:len(s) if e_idx == -1 else e_idx]
            f1 = self.isInteger(s1)

        if e_count == 1:

            s3 = s[e_idx+1:]
            f3 = self.isInteger(s3)
            if (not self.isEmpty(s[:e_idx]) and s[e_idx-1] == ' ') or (not self.isEmpty(s3) and s[e_idx+1] == ' '):
                return False
        return f1 and f2 and f3

obj = Solution()
s = '1e 1'
ans = obj.isNumber(s)
print(ans)